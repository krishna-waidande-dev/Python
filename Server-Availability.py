from os import stat
from platform import system
from subprocess import call
from datetime import datetime

server_names = ["www.google.com", "www.facebook.com", "www.google2.com", "www.google3.com"]
down_servers_file = r"C:\Users\Desktop\Python-Automation\server_downtime_list.txt"
available_servers = dict()
down_server_file_content_dic = dict()


def ping_to_server(host):
    if system().lower() == 'windows':
        command = ['ping', '-n', '3', host]
    else:
        command = ['ping', '-c', '3', host]
    return call(command) == 0


def load_file_in_dict():
    if stat(down_servers_file).st_size == 0:
        print("File is empty")
        return

    with open(down_servers_file, 'r+') as content:
        for line in content:
            #To eliminate blank lines
            if not line.isspace():
                row = line.split(',')
                server = row[0]
                downtime = row[1]
                down_server_file_content_dic[server] = downtime


def check_server_availability():
    down_server_flag = 0
    for server in server_names:
        if ping_to_server(server):
            if server in down_server_file_content_dic:
                available_servers[server] = str(datetime.now())
                del down_server_file_content_dic[server]
        else:
            if server not in down_server_file_content_dic:
                down_server_file_content_dic[server] = str(datetime.now())
                down_server_flag = 1

    if down_server_flag:
        send_mail_for_down_servers(down_server_file_content_dic)

    if available_servers:
        send_mail_for_up_servers(available_servers)


def send_mail_for_down_servers(down_server_list):
    print(down_server_list)


def send_mail_for_up_servers(up_server_list):
    print(up_server_list)


def write_dict_to_file():
    with open(down_servers_file, 'w+') as fileWrite:
        for server, timestamp in down_server_file_content_dic.items():
            fileWrite.write(server + ', ' + str(timestamp) + '\n')
   

def main():
    load_file_in_dict()
    check_server_availability()
    write_dict_to_file()


main()

