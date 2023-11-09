import math
import os
import random
import time
from datetime import datetime
import numpy as np
from matplotlib import pyplot as plt, axis
import matplotlib
import pandas as pd
from matplotlib.patches import Rectangle
from scipy.interpolate import make_interp_spline
from controller.database_io import db_query_data
from model.global_var import GlobalVar

"""
Author: GRP group 14
"""
path = "..\\..\\view\\img\\graph"

"""
Generate the formative data which is used to plot
"""
def data_integrate(dataframe, value_type):
    new_data = pd.DataFrame(columns=['time', 'value'])
    data = dataframe.sort_values(by="_time", ascending=True)
    # print(data)
    last = 0
    sum = 0
    items = 0
    i = 0
    print(len(data))
    if len(data) > 1:
        for index, value in data.iterrows():
            i += 1
            if last == 0:
                sum = value[value_type]
                items = 1
            elif last != 0 and value['_time'] == last and i != len(data):
                sum = sum + value[value_type]
                items += 1
            else:
                new_data = pd.concat([new_data, pd.DataFrame([[last, float(sum / items)]], columns=['time', 'value'])],
                                     ignore_index=True)
                sum = value[value_type]
                items = 1
            last = value['_time']
    else:
        new_data['time'] = data['_time']
        new_data['value'] = data['value']
    print(new_data)
    return new_data


"""
Calculate user's BMI
"""
def bmi_calculator(data):
    height = GlobalVar.get_value("height", "h")
    if len(height) == 0:
        return 0
    x = float(height)
    data['value'] = data['value']/(x * x * 0.0001)
    return data

"""
Plot the trend of user's health data
"""
def trend_plotter(mean_v, table, period):
    mean_y = mean_v['value'].tolist()
    x = mean_v['time'].astype(str).tolist()
    new_x = []
    for i in x:
        new_x.append(i[0:10])
    print(new_x)
    time = range(1, len(x)+1)

    fig = plt.figure(num=1, figsize=(10, 6))
    ax = fig.add_subplot(111)

    top = (int(np.max(mean_y) / 10) + 1) * 10
    bottom = (int(np.min(mean_y) / 10) -1) * 10

    model = make_interp_spline(time, mean_y)
    xs = np.linspace(time[0], time[len(time)-1], 500)
    ys = model(xs)

    ax.plot(time, mean_y, 'b', marker='o', lw=0)
    ax.plot(xs, ys, 'b', label='daily average')
    ax.fill_between(xs, bottom, ys, color='blue', alpha=.10)
    ax.plot(time[len(time)-1], mean_y[len(mean_y)-1], 'crimson', marker='o', lw=0, label="today: " + str(mean_y[len(mean_y)-1]))

    if period == "Week":
        plt.xticks(time, new_x)
    elif period == "Month":
        plt.xticks(time, new_x)

    ax.set_yticks(np.linspace(bottom, top, 5))

    ax.set_title(period + "ly trends")
    ax.set_xlabel("Time")

    if table == "hr":
        ax.set_ylabel("Heart Rate")
    elif table == "rhr":
        ax.set_ylabel("Resting Heart Rate")
    elif table == "bm":
        ax.set_ylabel("Weight (unit: Kg)")

    plt.legend()
    if not os.path.exists(path):
        os.makedirs(path)
    fig.savefig(os.path.join(path, table + "_trend_" + period + ".png"), dpi=300)
    plt.close(fig)

"""
Plot the bar chart formate of heart rate data
"""
def bar_chart_plotter_hr(mean_v, max_v, min_v, category, period):
    mean_y = mean_v['value'].tolist()
    max_y = max_v['value'].tolist()
    min_y = min_v['value'].tolist()
    time = mean_v['time'].tolist()
    diff = []
    for a, b in zip(max_y, min_y):
        diff.append(a - b)

    top = (int(np.max(max_y) / 10) + 1) * 10
    bottom = (int(np.min(min_y) / 10)) * 10

    fig = plt.figure(num=1, figsize=(10, 6))
    ax = fig.add_subplot(111)
    ax.set_title("Last Week")

    for x, y in zip(time, max_y):
        ax.text(x, y + (top - bottom) / 25, '%.2f' % y, ha='center', va='top')

    for x, y in zip(time, min_y):
        ax.text(x, y - (top - bottom) / 25, '%.2f' % y, ha='center', va='bottom')
    for x, y in zip(time, mean_y):
        ax.text(x, y + (top - bottom) / 25, '%.2f' % y, ha='center', va='bottom')

    ax.bar(time, diff, facecolor='blue', alpha=.10, width=0.65, bottom=min_y, label='HeartRate', )
    ax.bar(time, 0.05, facecolor='crimson', width=0.6, bottom=mean_y, label='Average')

    if category == "rhr":
        ax.set_ylabel("Resting Heart Rate")
    else:
        ax.set_ylabel("Heart Rate")
    ax.set_xlabel("Days")
    ax.xaxis_date()
    ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%Y-%m-%d"))
    ax.set_yticks(np.linspace(bottom, top, 5))

    plt.legend()
    if not os.path.exists(path):
        os.makedirs(path)
    fig.savefig(os.path.join(path, category + "_" + period + ".png"), dpi=300)
    plt.close(fig)

"""
Plot the bar chart formate of blood pressure data
"""
def bar_chart_plotter_bp(max_v, min_v, period):
    max_y = max_v['value'].tolist()
    min_y = min_v['value'].tolist()
    axis_x = max_v['time'].tolist()
    diff = []
    for a, b in zip(max_y, min_y):
        diff.append(a - b)

    top = (int(np.max(max_y) / 10) + 1) * 10
    bottom = (int(np.min(min_y) / 10) - 1) * 10

    fig = plt.figure(num=1, figsize=(10, 6))
    ax = fig.add_subplot(111)
    ax.set_title("Last " + period)

    marker1 = 0
    marker2 = 0
    marker3 = 0
    for x, y1, y2 in zip(axis_x, max_y, min_y):
        if 140 < y1 < 180 or 90 < y2 < 100:
            if marker1 == 0:
                ax.bar(x, y1 - y2, facecolor='crimson', alpha=.10, width=0.65, bottom=y2, label='Abnormal')
                marker1 = -1
            else:
                ax.bar(x, y1 - y2, facecolor='crimson', alpha=.10, width=0.65, bottom=y2)
            ax.plot(x, y1, c='crimson', marker='|', ms=5)
            ax.plot(x, y2, c='crimson', marker='|', ms=5)
        elif 90 < y1 < 120 and 60 < y2 < 80:
            if marker2 == 0:
                ax.bar(x, y1 - y2, facecolor='blue', alpha=.10, width=0.65, bottom=y2, label='Normal')
                marker2 = -1
            else:
                ax.bar(x, y1 - y2, facecolor='blue', alpha=.10, width=0.65, bottom=y2)
            ax.plot(x, y1, c='royalblue', marker='|', ms=5)
            ax.plot(x, y2, c='royalblue', marker='|', ms=5)
        else:
            if marker3 == 0:
                ax.bar(x, y1 - y2, facecolor='orange', alpha=.20, width=0.65, bottom=y2, label='Sub-normal')
                marker3 = -1
            else:
                ax.bar(x, y1 - y2, facecolor='orange', alpha=.20, width=0.65, bottom=y2)
            ax.plot(x, y1, c='orange', marker='|', ms=5)
            ax.plot(x, y2, c='orange', marker='|', ms=5)

    mid_x = (axis_x[len(axis_x) - 1] - axis_x[0]) / 2 + axis_x[0]
    total_width = pd.DataFrame([[axis_x[len(axis_x) - 1] - axis_x[0]]], columns=['delta'], dtype='timedelta64[D]')
    total_width['delta'].astype('float64')
    tw = total_width['delta'].tolist()[0]
    ax.bar([mid_x] * 1, 20, facecolor='seagreen', alpha=.15, width=tw + 0.65, bottom=60, label='Ideal')
    ax.bar([mid_x] * 1, 30, facecolor='seagreen', alpha=.15, width=tw + 0.65, bottom=90)

    # ax.plot(axis_x[0], max_y[0], c='cornflowerblue', marker='^', ms=5, label='Systolic',lw=0)
    # ax.plot(axis_x[0], min_y[0], c='cornflowerblue', marker='v', ms=5, label='Diastolic',lw=0)

    ax.set_ylabel("Blood Pressure")
    ax.set_xlabel("Time")
    ax.xaxis_date()
    ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%Y-%m-%d"))
    if period == "Week":
        plt.xticks(pd.date_range(axis_x[0], axis_x[len(axis_x) - 1], freq='1d'))
    elif period == "Month":
        plt.xticks(pd.date_range(axis_x[0], axis_x[len(axis_x) - 1], freq='5d'))
    elif period == "Hour":
        plt.xticks(pd.date_range(axis_x[0], axis_x[len(axis_x) - 1], freq='5m'))

    ax.set_yticks(np.linspace(bottom, top, 5))
    plt.legend()
    if not os.path.exists(path):
        os.makedirs(path)
    fig.savefig(os.path.join(path, "bp_" + period + ".png"), dpi=300)
    plt.close(fig)

"""
Plot the line chart formate of user's health data
"""
def line_chart_plotter(data, table, period):
    x = data['time'].tolist()
    y = data['value'].tolist()
    mean = [np.sum(y) / len(y)] * len(y)

    print(x)

    max_indx = np.argmax(y)  # max value index
    min_indx = np.argmin(y)

    top = (int(y[max_indx] / 10) + 1) * 10
    bottom = (int(y[min_indx] / 10) - 1) * 10

    fig = plt.figure(num=1, figsize=(10, 6))
    ax = fig.add_subplot(111)

    ax.plot(x, y, label='Heart Rate', c='blue', marker='o', ms=4, linewidth=1)

    ax.legend(loc=1, handlelength=2)
    ax.plot(x, mean, 'crimson', label="Average: " + str(int(mean[0])))
    ax.plot(x[max_indx], y[max_indx], c='crimson', marker='o', ms=5, label='Max')
    ax.plot(x[min_indx], y[min_indx], c='orange', marker='o', ms=5, label='Min')
    ax.text(x[max_indx], y[max_indx] + (top - bottom) / 20, str(int(y[max_indx])), ha='center', va='top')
    ax.text(x[min_indx], y[min_indx] - (top - bottom) / 20, str(int(y[min_indx])), ha='center', va='top')
    ax.fill_between(x, bottom, y, color='blue', alpha=.10)

    ax.set_title("Last " + period)
    ax.set_xlabel("Time")
    if table == "hr":
        ax.set_ylabel("Heart Rate")
    elif table == "rhr":
        ax.set_ylabel("Resting Heart Rate")
    elif table == "bm":
        ax.set_ylabel("Weight")

    ax.xaxis_date()

    ax.set_yticks(np.linspace(bottom, top, 5))

    if period == "Week":
        plt.xticks(pd.date_range(x[0], x[len(x) - 1], freq='1d'))
        ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%Y-%m-%d"))
    elif period == "Month":
        plt.xticks(pd.date_range(x[0], x[len(x) - 1], freq='5d'))
        ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%Y-%m-%d"))
    elif period == "Hour":
        plt.xticks(pd.date_range(x[0], x[len(x) - 1], freq='10m'))
        ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%H:%M:%S"))
    elif period == "Day":
        plt.xticks(pd.date_range(x[0], x[len(x) - 1], freq='4h'))
        ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%d %H:%M"))
    plt.legend()
    if not os.path.exists(path):
        os.makedirs(path)
    fig.savefig(os.path.join(path, table + "_" + period + ".png"), dpi=300)
    plt.show()
    plt.close(fig)

"""
Plot the user's BMI data
"""
def bmi_plotter(data):
    print("hello")
    data = data['value'].tolist()[0]
    print(data)
    fig = plt.figure(num=1, figsize=(8, 1))
    ax = fig.add_subplot(111)

    # ax.text(data+1, 0.74, "NEW", color="darkred")
    if data < 18.5:
        ax.plot(data, 1, c='slateblue', marker='o', ms=10, linewidth=1)
    elif data >= 18.5 and data<=24.9:
        ax.plot(data, 1, c='seagreen', marker='o', ms=10, linewidth=1)
    elif data > 24.9 and data <=30:
        ax.plot(data, 1, c='orangered', marker='o', ms=10, linewidth=1)
    elif data > 30:
        ax.plot(data, 1, c='crimson', marker='o', ms=10, linewidth=1)

    ax.bar(18.5/2, 2, facecolor='slateblue', alpha=.15, width=18.5, bottom=0)
    ax.bar(21.7, 2, facecolor='seagreen', alpha=.15, width=6.4, bottom=0)
    ax.bar(27.45, 2, facecolor='orangered', alpha=.15, width=5.1, bottom=0)
    if data>30:
        ax.bar((data-30)/2 + 30, 2, facecolor='crimson', alpha=.15, width=data-30, bottom=0)
        index_ls = ['Underweight', 'Normal Weight', 'Overweight','Obesity']
        plt.xticks([9.25, 21.7, 27.45,(data-30)/2 + 30], index_ls)
    else:
        index_ls = ['Underweight','Normal Weight','Overweight']
        plt.xticks([9.25,21.7,27.45],index_ls)
     # ax.fill_etween(x, bottom, y, color='blue', alpha=.10)

    ax.set_title("Today's BMI")
    plt.xlim(0, None)
    # ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%H:%M"))
    plt.yticks([])  # delete y axis
    ax.axis('scaled')

    if not os.path.exists(path):
        os.makedirs(path)
    fig.savefig(os.path.join(path, "BMI_day.png"), dpi=300)
    plt.close(fig)

"""
Plot the trend of the BMI data
"""
def bmi_trend_plotter(data, period):
    x = data['time'].tolist()
    y = data['value'].tolist()
    print(y)
    mean = [np.sum(y) / len(y)] * len(y)

    max_indx = np.argmax(y)  # max value index
    min_indx = np.argmin(y)

    top = (int(y[max_indx] / 10) + 1) * 10
    bottom = (int(y[min_indx] / 10) - 1) * 10

    fig = plt.figure(num=1, figsize=(10, 6))
    ax = fig.add_subplot(111)

    ax.plot(x, y, label='BMI', c='blue', marker='o', ms=4, linewidth=1)

    ax.legend(loc=1, handlelength=2)
    mid_x = (x[len(x) - 1] - x[0]) / 2 + x[0]
    total_width = pd.DataFrame([[x[len(x) - 1] - x[0]]], columns=['delta'], dtype='timedelta64[D]')
    total_width['delta'].astype('float64')
    tw = total_width['delta'].tolist()[0]
    ax.bar([mid_x] * 1, 6.4, facecolor='seagreen', alpha=.15, width=tw, bottom=18.5, label='Normal Weight = 18.5–24.9')
    ax.bar([mid_x] * 1, 18.5-bottom, facecolor='slateblue', alpha=.15, width=tw, bottom=bottom, label='Underweight =<18.5')
    ax.bar([mid_x] * 1, 5, facecolor='orangered', alpha=.15, width=tw, bottom=24.9, label='Overweight = 25–29.9')
    ax.bar([mid_x] * 1, top - 29.9, facecolor='crimson', alpha=.15, width=tw, bottom = 29.9, label='Obesity >= 30')

    ax.plot(x[max_indx], y[max_indx], c='crimson', marker='o', ms=5, label='Max')
    ax.plot(x[min_indx], y[min_indx], c='orange', marker='o', ms=5, label='Min')
    ax.text(x[max_indx], y[max_indx] + (top - bottom) / 20, str(int(y[max_indx])), ha='center', va='top')
    ax.text(x[min_indx], y[min_indx] - (top - bottom) / 20, str(int(y[min_indx])), ha='center', va='top')
    # ax.fill_between(x, bottom, y, color='blue', alpha=.10)

    ax.set_title("Last " + period)

    ax.xaxis_date()
    # ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%H:%M"))

    ax.set_yticks(np.linspace(bottom, top, 5))
    ax.set_xlabel("Days")
    ax.set_ylabel("BMI (unit: Kg/M^2)")

    if period == "Week":
        plt.xticks(pd.date_range(x[0], x[len(x) - 1], freq='1d'))
        ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%Y-%m-%d"))
    elif period == "Month":
        plt.xticks(pd.date_range(x[0], x[len(x) - 1], freq='5d'))
        ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%Y-%m-%d"))

    plt.legend()
    if not os.path.exists(path):
        os.makedirs(path)
    fig.savefig(os.path.join(path,  "BMI_" + period + ".png"), dpi=300)
    plt.close(fig)

"""
Plot the bar chart formate of blood pressure data
"""
def bp_plotter(data):

    # get the length of input data
    length = len(data)

    # define Matplotlib figure and axis
    fig = plt.figure(num=1, figsize=(10, 6))
    ax = fig.add_subplot(111)


    # add rectangle plot of high blood pressure range
    ax.add_patch(Rectangle((40, 70), 60, 120,
                           facecolor='salmon',
                           fill=True,
                           lw=5))
    ax.text(40.5, 186.5, "High Blood Pressure", fontsize=12, color="brown")

    # add rectangle plot of pre-high blood pressure range
    ax.add_patch(Rectangle((40, 70), 50, 70,
                           facecolor='sandybrown',
                           fill=True,
                           lw=5))
    ax.text(40.5, 136.5, "Pre-High Blood Pressure", fontsize=12, color="firebrick")

    ax.add_patch(Rectangle((40, 70), 40, 50,
                           facecolor='bisque',
                           fill=True,
                           lw=5))
    ax.text(40.5, 116.5, "Part-High Blood Pressure", fontsize=12, color="darkgoldenrod")

    # add rectangle plot of normal/ideal blood pressure range
    ax.add_patch(Rectangle((60, 90), 20, 30,
                           facecolor='olivedrab',
                           fill=True,
                           lw=5))
    ax.text(60.5, 116.5, "Ideal Blood Pressure", fontsize=12, color="white")

    # add rectangle plot of low blood pressure range
    ax.add_patch(Rectangle((40, 70), 20, 20,
                           facecolor='cornflowerblue',
                           fill=True,
                           lw=5))
    ax.text(40.5, 86.5, "Low Blood Pressure", fontsize=12, color="midnightblue", alpha=0.75)

    ax.plot(data[1], data[0], marker="o", color="darkred")
    ax.text(data[1],
            data[0] + 3.5,
            "NEW MEASUREMENT",
            fontsize=12,
            fontweight="bold",
            color="darkred",
            horizontalalignment="center")

    # set the label of x-axis and y-axis
    plt.title("Today", fontsize=13)
    plt.xlabel("Diastolic (bottom number, unit: mmHg)", fontsize=13)
    plt.ylabel("Systolic (top number, unit: mmHg)", fontsize=13)

    plt.xlim(40, 100)
    plt.ylim(70, 190)

    fig.savefig(os.path.join(path, "bp_day.png"), dpi=300)
    plt.close(fig)

"""
Plot all the weekly health report graph
"""
def weekly_report_producer():
    hr = db_query_data.get_specified_value("-8d", "-0d", "1d", "mean", "HeartRate")
    bm = db_query_data.get_specified_value("-8d", "-0d", "1d", "mean", "Weight")
    bp_mean_sys = db_query_data.get_specified_value_pro("-8d", "-0d", "1d", "mean", "BloodPressure", "systolic")
    bp_mean_dia = db_query_data.get_specified_value_pro("-8d", "-0d", "1d", "mean", "BloodPressure", "diastolic")

    if hr.empty or bm.empty or bp_mean_dia.empty or bp_mean_sys.empty:
        print("[INFO] The report could not be displayed properly due to insufficient data.")
        return 0

    hr = data_integrate(hr, 'value')
    bm = data_integrate(bm, 'value')
    bm = bmi_calculator(bm)
    bp_mean_dia = data_integrate(bp_mean_dia, 'diastolic')
    bp_mean_sys = data_integrate(bp_mean_sys, 'systolic')

    bar_chart_plotter_bp(bp_mean_sys, bp_mean_dia, "Week")
    line_chart_plotter(hr, "rhr", "Week")
    bmi_trend_plotter(bm, "Week")
    return 1

"""
Plot all the monthly health report graph
"""
def monthly_report_producer():
    hr = db_query_data.get_specified_value("-31d", "-0d", "1d", "mean", "HeartRate")
    bm = db_query_data.get_specified_value("-31d", "-0d", "1d", "mean", "Weight")
    bp_mean_sys = db_query_data.get_specified_value_pro("-31d", "-0d", "1d", "mean", "BloodPressure", "systolic")
    bp_mean_dia = db_query_data.get_specified_value_pro("-31d", "-0d", "1d", "mean", "BloodPressure", "diastolic")

    if hr.empty or bm.empty or bp_mean_dia.empty or bp_mean_sys.empty:
        print("[INFO] The report could not be displayed properly due to insufficient data.")
        return 0

    hr = data_integrate(hr, 'value')
    bm = data_integrate(bm, 'value')
    bm = bmi_calculator(bm)
    bp_mean_dia = data_integrate(bp_mean_dia, 'diastolic')
    bp_mean_sys = data_integrate(bp_mean_sys, 'systolic')

    bar_chart_plotter_bp(bp_mean_sys, bp_mean_dia, "Month")
    line_chart_plotter(hr, "rhr", "Month")
    bmi_trend_plotter(bm, "Month")
    return 1

"""
Plot weight graph in health report
"""
def bm_report_producer():
    bm_week = db_query_data.get_specified_value("-7d", "-0d", "1d", "mean", "Weight")
    bm_week = data_integrate(bm_week, 'value')
    bm_day = db_query_data.get_specified_value("-1d", "-0d", "1d", "mean", "Weight")
    if bm_week.empty or bm_day.empty:
        print("[INFO] The report could not be displayed properly due to insufficient data.")
        return 0
    bmi = bmi_calculator(bm_day)
    # print(bmi)
    bmi_plotter(bmi)
    trend_plotter(bm_week, "bm", "Week")
    return 1

"""
Plot blood pressure graph in health report
"""
def bp_report_producer():
    bp_mean_sys = db_query_data.get_specified_value_pro("-1d", "-0d", "1d", "mean", "BloodPressure", "systolic")
    bp_mean_dia = db_query_data.get_specified_value_pro("-1d", "-0d", "1d", "mean", "BloodPressure", "diastolic")
    if bp_mean_dia.empty or bp_mean_sys.empty:
        print("[INFO] The report could not be displayed properly due to insufficient data.")
        return 0
    bp = [bp_mean_sys['systolic'].tolist()[0], bp_mean_dia['diastolic'].tolist()[0]]
    bp_plotter(bp)
    return 1

"""
Plot heart rate graph in health report
"""
def hr_report_hour():
    hr = db_query_data.get_specified_value("0h", "8h", "1m", "mean", "HeartRate")
    if hr.empty:
        print("[INFO] The report could not be displayed properly due to insufficient data.")
        return 0
    hr = data_integrate(hr, 'value')
    line_chart_plotter(hr, "hr", "Hour")

"""
Plot 24 hours heart rate graph in health report
"""
def hr_report_24hour():
    hr = db_query_data.get_specified_value("-16h", "8h", "15m", "mean", "HeartRate")
    if hr.empty:
        print("[INFO] The report could not be displayed properly due to insufficient data.")
        return 0
    hr = data_integrate(hr, 'value')
    line_chart_plotter(hr, "hr", "Day")


if __name__ == '__main__':
    # bm_report_producer()
    # weekly_report_producer()
    # monthly_report_producer()
    hr_report_24hour()
    hr_report_hour()
