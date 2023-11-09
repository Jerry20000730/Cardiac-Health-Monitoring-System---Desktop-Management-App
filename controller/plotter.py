import pandas as pd
import matplotlib.pyplot as plt
from pylab import *
from matplotlib.patches import Rectangle
import controller
from model.temp_data import SimData
from controller.utility import Utility

"""
Author: GRP group 14
"""
# set the parameters for plotting
mpl.rcParams['figure.dpi'] = 300
plt.rcParams["figure.figsize"] = (5, 5)

# ignore the warning message
import warnings

warnings.filterwarnings("ignore")


class Plotter(object):
    """
    * This is the class for visualizing data/results from measurements 
    """

    def plot_BP(self, data, display_mode, saveto):
        """
        * The method to plot blood pressure data with different range
        TODO: The scale of x-axis and y-axis should auto adjust according to the data in further development
        @param self: the instance of Plotter class
        @param data: the blood pressure data (format: DataFrame)
        @param saveto: whether to save the output figure, example:
            {True: save the figure to default location,
             False: don't save the output figure,
             "filepath": save the figure to the target filepath}
        """

        filepath_dict = {"new": "model/result/bp_day.png",
                         "history": "model/result/blood_pressure_history.png"}

        # get the length of input data
        length = len(data)

        # define Matplotlib figure and axis
        fig = plt.figure(num=1, figsize=(10, 6))
        ax = fig.add_subplot(111)

        if length >= 1:

            if display_mode == "history":

                # plot the data points from 0 to (length-1) in DataFrame
                for i in range(0, length - 1):
                    plt.plot(data["diastolic"][i],
                             data["systolic"][i],
                             marker='o',
                             markersize=5,
                             color="black",
                             alpha=1)

            # plot the data point of newest measurment (tail of the DataFrame)
            plt.plot(data["diastolic"].tail(1),
                     data["systolic"].tail(1),
                     marker='o',
                     markersize=5,
                     color="darkred")

            # add the label of newest measurment (tail of the DataFrame)
            ax.text(data["diastolic"].tail(1),
                    data["systolic"].tail(1) + 3.5,
                    "NEW MEASUREMENT",
                    fontsize=7.5,
                    fontweight="bold",
                    color="darkred",
                    horizontalalignment="center")

        # add rectangle plot of high blood pressure range
        ax.add_patch(Rectangle((40, 70), 60, 120,
                               facecolor='salmon',
                               fill=True,
                               lw=5))
        ax.text(40.5, 186.5, "High Blood Pressure", fontsize=7.5, color="brown")

        # add rectangle plot of pre-high blood pressure range
        ax.add_patch(Rectangle((40, 70), 50, 70,
                               facecolor='bisque',
                               fill=True,
                               lw=5))
        ax.text(40.5, 136.5, "Pre-High Blood Pressure", fontsize=7.5, color="darkgoldenrod")

        ax.add_patch(Rectangle((40, 70), 40, 50,
                               facecolor='lavender',
                               fill=True,
                               lw=5))
        ax.text(40.5, 116.5, "Part-High Blood Pressure", fontsize=7.5, color="black")

        # add rectangle plot of normal/ideal blood pressure range
        ax.add_patch(Rectangle((60, 90), 20, 30,
                               facecolor='yellowgreen',
                               fill=True,
                               lw=5))
        ax.text(60.5, 116.5, "Ideal Blood Pressure", fontsize=7.5, color="darkolivegreen")


        # add rectangle plot of low blood pressure range
        ax.add_patch(Rectangle((40, 70), 20, 20,
                               facecolor='cornflowerblue',
                               fill=True,
                               lw=5))
        ax.text(40.5, 86.5, "Low Blood Pressure", fontsize=7.5, color="midnightblue", alpha=0.75)

        # set the label of x-axis and y-axis
        plt.xlabel("Diastolic (bottom number, unit: mmHg)")
        plt.ylabel("Systolic (top number, unit: mmHg)")

        plt.xlim(40, 100)
        plt.ylim(70, 190)

        # save the figure to default location
        if saveto == True:
            plt.savefig(filepath_dict[display_mode],
                        transparent=True,
                        bbox_inches="tight")
        # do not save the figure but show in the terminal
        elif saveto == False:
            plt.show()
        # save to customized location
        else:
            plt.savefig(saveto + filepath_dict[display_mode],
                        transparent=True,
                        bbox_inches="tight")

        print("[INFO] Successfully generated the new blood pressure figure. Display mode: " + display_mode + ".")

    def plot_resting_HR(self, data, saveto):
        """
        * The method to plot resting heart rate data with different range
        ! It is assumed that the data contains one average HR value in each single day.
        ! The method will select only last 30 data points (days) to plot the trend figure.
        TODO: Timestamp and scale of the figure should be adjusted in the further devleopment
        @param self: the instance of Plotter class
        @param data: the resting heart rate data (format: DataFrame)
        @param saveto: whether to save the output figure, example:
            {True: save the figure to default location,
             False: don't save the output figure,
             "filepath": save the figure to the target filepath}
        """

        # select the last 30 data points from input data
        length = len(data)
        if length > 30:
            data = data.tail(30)
            length = len(data)

        max_HR = data["HR/sec (round, de-nan)"].max()  # calculate the maximum value of the data
        min_HR = data["HR/sec (round, de-nan)"].min()  # calculate the minimum value of the data
        last_HR = data["HR/sec (round, de-nan)"].iloc[-1]  # get the last data point from the data
        avg_7 = data["HR/sec (round, de-nan)"].tail(7).mean()  # calculate the average value of last 7 data points
        avg_14 = data["HR/sec (round, de-nan)"].tail(14).mean()  # calculate the average value of last 14 data points
        avg_30 = data["HR/sec (round, de-nan)"].tail(30).mean()  # calculate the average value of last 30 data points

        # define Matplotlib figure and axis
        fig, ax = plt.subplots()

        # plot the line chart of resting heart rate data
        plt.plot(data["HR/sec (round, de-nan)"],
                 color="indianred",
                 linewidth=2,
                 marker='o',
                 markersize=2)
        ax.text(length + 0.5, last_HR - 0.15, str(last_HR), fontsize=5, fontweight="bold", color="indianred")

        # plot the average line of last 7 days (data points) resting heart rate
        plt.plot([length - 7, length], [avg_7, avg_7], linewidth=2.5, alpha=1, color="steelblue")
        ax.text(length - 7, avg_7 + 0.25, "7D AVG", fontsize=5, fontweight="bold", color="steelblue")
        ax.text(length + 0.5, avg_7 - 0.15, str(round(avg_7)), fontsize=5, fontweight="bold", color="steelblue")

        # plot the average line of last 14 days (data points) resting heart rate
        plt.plot([length - 14, length], [avg_14, avg_14], linewidth=2.5, alpha=1, color="olivedrab")
        ax.text(length - 14, avg_14 + 0.25, "14D AVG", fontsize=5, fontweight="bold", color="olivedrab")
        ax.text(length + 0.5, avg_14 - 0.15, str(round(avg_14)), fontsize=5, fontweight="bold", color="olivedrab")

        # plot the average line of last 30 days (data points) resting heart rate
        plt.plot([length - 30, length], [avg_30, avg_30], linewidth=2.5, alpha=1, color="dimgrey")
        ax.text(length - 30, avg_30 + 0.25, "30D AVG", fontsize=5, fontweight="bold", color="dimgrey")
        ax.text(length + 0.5, avg_30 - 0.15, str(round(avg_30)), fontsize=5, fontweight="bold", color="dimgrey")

        # add legend into the figure
        plt.legend(labels=["Average Heart Rate",
                           "7 Days Average HR",
                           "14 Days Average HR",
                           "30 Days Average HR"],
                   loc="best",
                   fontsize=5)

        # set the labels of x-axis and y-axis
        plt.xlabel("Day")
        plt.ylabel("Average Heart Rate (unit: BPM)")

        # limit the scale of y-axis according to the maximum and minimum heart rate values
        plt.ylim([int(min_HR * 0.9), int(max_HR * 1.1)])

        # save the figure to default location
        if saveto == True:
            plt.savefig("model/result/heart_rate_trends_new.png",
                        transparent=True,
                        bbox_inches="tight")
        # do not save the figure but show in the terminal
        elif saveto == False:
            plt.show()
        # save to customized location
        else:
            plt.savefig(saveto + "heart_rate_trends_new.png",
                        transparent=True,
                        bbox_inches="tight")

        print("[INFO] Successfully generated the new resting heart rate figure.")

    def plot_weight_trends(self, data, goal, plot_type, saveto):
        """
        * The method to plot body weight trends in a continuous bar chart
        @param self: the instance of Plotter class
        @param data: the body weight trends (format: DataFrame)
        @param goal: the goal of weight management
        @param saveto: whether to save the output figure, example:
            {True: save the figure to default location,
             False: don't save the output figure,
             "filepath": save the figure to the target filepath}
        """

        # select the last 30 data points from input data
        length = len(data)
        if length > 30:
            data = data.tail(30)
            length = len(data)

        # reset the size of output figure
        plt.rcParams["figure.figsize"] = (5, 3.5)

        # define Matplotlib figure and axis
        fig, ax = plt.subplots()

        if plot_type == "barchart":
            # plot the bar chart of everyday's weight data (from minimum to maximum)
            for i in range(0, length):
                BM = plt.plot([data["Date"][i], data["Date"][i]],
                              [data["MIN BM"][i], data["MAX BM"][i]],linewidth=5,
                              alpha=1,
                              color="steelblue")

            # plot the line of weight management goal  
            if goal != False:
                plt.plot([data["Date"][0], data["Date"].iloc[-1]], [goal, goal], linewidth=2.5, alpha=1, color="gold")
                ax.text(length, goal,
                        " YOUR\n GOAL",
                        fontsize=7.5,
                        fontweight="bold",
                        color="gold",
                        verticalalignment="center",
                        horizontalalignment="center")

        elif plot_type == "linechart":
            avg_7 = data["value"].tail(7).mean()  # calculate the average value of last 7 data points
            plt.plot(data["time"], data["value"])
            plt.plot([length - 7, length], [avg_7, avg_7], linewidth=2.5, alpha=1, color="red")
            ax.text(length - 7, avg_7 + 0.25, "7D AVG", fontsize=5, fontweight="bold", color="red")
            ax.text(length + 0.5, avg_7 - 0.15, str(round(avg_7)), fontsize=5, fontweight="bold", color="red")

        # set the labels of x-axis and y-axis
        plt.xlabel("Date")
        plt.ylabel("Body Mass (unit: KG)")

        # rotation the text of values in x-axis
        plt.xticks(rotation=90, fontsize=7.5)

        # save the figure to default location
        if saveto == True:
            plt.savefig("model/result/body_mass_trends_new.png",
                        transparent=True,
                        bbox_inches="tight")

        # do not save the figure but show in the terminal
        elif saveto == False:
            plt.show()
        # save to customized location
        else:
            plt.savefig(saveto + "body_mass_trends_new.png",
                        transparent=True,
                        bbox_inches="tight")

        print("[INFO] Successfully generated the new weight figure.")

    def plot_HR_assessment(self, data, reference, saveto):
        """
        * The method to plot heart rate assessment results with different range
        ? The ranges of green/yellow/red cirles are manually defined in this stage
        @param self: the instance of Plotter class
        @param data: the heart rate assessment results (format: DataFrame)
        @param reference: whether to show the references of unhealthy samples, example: {True, False}
        @param saveto: whether to save the output figure, example:
            {True: save the figure to default location,
             False: don't save the output figure,
             "filepath": save the figure to the target filepath}
        """

        # get the length of input data
        length = len(data)

        # get the centers from each group (health status) of data
        centers = data.groupby(by=["Status"]).mean()

        # define Matplotlib figure and axis
        fig, ax = plt.subplots()

        # define the color of each class of health status
        colors_map = (["Normal", "darkgreen"],
                      ["Hypertensive", "salmon"],
                      ["Congestive Heart Failure", "peru"],
                      ["Your Assessment", "black"])
        colors_map = pd.DataFrame(colors_map, columns=["Status", "Color"])

        # group the data by the health status label
        groups = data.groupby("Status")

        # plot the range of normal heart health assessment
        plt.plot(centers["STD"]["Normal"],
                 centers["Distance"]["Normal"],
                 marker='o',
                 markersize=800,
                 color="lightsalmon")

        # plot the range of yellow-zone heart health assessment
        plt.plot(centers["STD"]["Normal"],
                 centers["Distance"]["Normal"],
                 marker='o',
                 markersize=370,
                 color="lightyellow")

        # plot the range of rate-zone heart health assessment
        plt.plot(centers["STD"]["Normal"],
                 centers["Distance"]["Normal"],
                 marker='o',
                 markersize=45,
                 color="lightgreen")

        # plot data points of assessments from each classes with different colors
        for name, group in groups:

            # plot the reference data points of unhealthy samples
            if reference == True:

                # set the filename
                filename = "heart_rate_assessment_new_reference.png"

                ax.plot(group["STD"], group["Distance"],
                        marker='o',
                        linestyle='',
                        label=name,
                        color=colors_map.loc[colors_map["Status"] == name]["Color"].item())

            # do not plot the reference data points of unhealthy samples
            else:

                # set the filename
                filename = "heart_rate_assessment_new.png"

                # only plot the results of the assessment of the user
                # TODO: the name might be changed in the further development
                if name == "Your Assessment":
                    ax.plot(group["STD"], group["Distance"],
                            marker='o',
                            linestyle='',
                            label=name,
                            color=colors_map.loc[colors_map["Status"] == name]["Color"].item())

        # set the legend, and labels of x-axis and y-axis
        ax.legend()
        plt.xlabel("Variability of Heart Rate")
        plt.ylabel("Stability Range of the Variability")

        # limit the scale of x-axis and y-axis according to the minimum and maximum values
        plt.xlim(0, data["STD"].max() * 1.1)
        plt.ylim(0, data["Distance"].max() * 1.1)

        # save the figure to default location
        if saveto == True:
            plt.savefig("model/result/" + filename,
                        transparent=True,
                        bbox_inches="tight")
        # do not save the figure but show in the terminal
        elif saveto == False:
            plt.show()
        # save to customized location
        else:
            plt.savefig(saveto + filename,
                        transparent=True,
                        bbox_inches="tight")

        print("[INFO] Successfully generated the new heart rate assessment figure.")

    def generate_BP_sim(self, saveto):
        """
        * The method to generate blood pressure plot with different range
        @param self: the instance of Plotter class
        @param saveto: whether to save the output figure, example:
            {True: save the figure to default location,
             False: don't save the output figure,
             "filepath": save the figure to the target filepath}
        """

        # initialize the simulated data object
        temp_data = SimData()
        # call method to plot the blood pressure figure


        self.plot_BP(temp_data.bp_data, saveto)

    def generate_BP_plot(self, result_range,  saveto):

        device_name = "Manually Input"
        start_time = "-30d"
        stop_time = "-0d"
        temp_data = SimData()
        #bp_data = controller.data_io.DataIO.get_bp_from_db(device_name, start_time, stop_time)
        self.plot_BP(temp_data.bp_data, result_range, saveto)

    def generate_HR_trends(self, saveto):
        """
        * The method to generate resting heart rate trends figure
        @param self: the instance of Plotter class
        @param saveto: whether to save the output figure, example:
            {True: save the figure to default location,
             False: don't save the output figure,
             "filepath": save the figure to the target filepath}
        """

        # initialize the simulated data object
        temp_data = SimData()

        # call method to plot the resting heart rate trends figure
        self.plot_resting_HR(plot,temp_data.hr_data, saveto)

    def generate_BM_trends(self, sim_data, goal, saveto):
        """
        * The method to generate body weight trends figure
        @param self: the instance of Plotter class
        @param saveto: whether to save the output figure, example:
            {True: save the figure to default location,
             False: don't save the output figure,
             "filepath": save the figure to the target filepath}
        """

        if sim_data:
            
            # initialize the simulated data object
            temp_data = SimData()

            # set the goal of weight management
            #

            # call method to plot the weight trends figure
            self.plot_weight_trends(temp_data.bm_data, goal, "linechart", saveto)
            
        else:
            
            device_name = "Manually Input"
            start_time = "-30d"
            stop_time = "-0d"
            # goal = 50.5

            bm_data = controller.data_io.DataIO.get_bm_from_db(device_name, start_time, stop_time)
            self.plot_weight_trends(bm_data, goal, "linechart", saveto)

    def generate_HR_assessment(self, reference, saveto):
        """
        * The method to generate heart rate assessment figure
        @param self: the instance of Plotter class
        @param saveto: whether to save the output figure, example:
            {True: save the figure to default location,
             False: don't save the output figure,
             "filepath": save the figure to the target filepath}
        """

        # initialize the simulated data object
        temp_data = SimData()

        # call method to plot the heart rate assessment figure
        self.plot_HR_assessment(temp_data.hr_assessment_data, reference, saveto)
