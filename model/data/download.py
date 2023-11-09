import paramiko
import os
from Counter import Counter


class Downlaod(object):
    # hostname = '192.168.3.6'

    def download(self):
        hostname = '1.116.223.195'
        port = 22
        username = 'root'
        password = 'gfc20000730'
        remote_path = '/home/grp_remote_repository'
        local_path = "C:\\Users\\Lenovo\\Desktop\\GRP\\shh-edge-computer\\model\\data_dir"
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=hostname, port=port, username=username, password=password)

        sftp_client = client.open_sftp()
        remote_file = sftp_client.listdir(remote_path)

        print(len(remote_file))

        Counter.init_bar_counter(self,len(remote_file)*6)
        print(Counter.get_counter(self))
        for dir_name in remote_file:
            remote_dir_path = remote_path + "/" + dir_name
            detail_files = sftp_client.listdir(remote_dir_path)
            local_file_path = local_path + "\\" + dir_name
            if not os.path.exists(local_file_path):
                os.mkdir(local_file_path)
                for detail_file in detail_files:
                    remote_file_path = remote_dir_path + "/" + detail_file
                    local_file_paths = local_file_path + "\\" + detail_file
                    print(local_file_paths)
                    sftp_client.get(remote_file_path, local_file_paths)
                    Counter.add_process_counter(self)
                    print(Counter.get_counter(self))
                    print(Counter.get_process_counter(self))
                   # Ui_MainWindow.update_data_progress_bar.setValue(Counter.get_process_counter())

    """stat() 查看服务器文件状态
    listdir() 列出服务器目录下的文件"""
if __name__ == "__main__":
    # print(Counter.get_process_counter(Downlaod))
    Downlaod.download(Downlaod)


