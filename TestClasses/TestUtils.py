import psutil
import os

WELCOME_TXT = "220 Welcome to Paradise"
PROCESS_NAME = "paradise_ftp"
DEFAULT_USER = "user"
DEFAULT_PASSWORD = "secret"
DEFAULT_PORT = 2121
DEFAULT_HOSTNAME = "localhost"


def get_pid(process_name):
    op = -1
    for proc in psutil.process_iter():
        if proc.name() == process_name:
            op = proc.pid
            break
    return op


def get_ftp_connection():
    from get_ftp_connection import TestGetFTPConnection
    return TestGetFTPConnection().get_authentication()


def generate_file(file_name, content):
    f = open(file_name, 'w')
    f.write(content)
    f.close()
    return os.path.join(os.getcwd(), file_name)


def delete_generated_file(file_name):
    os.remove(file_name)


def get_str(n):
    dict_a = {1: "st", 2: "nd", 3: "rd"}
    op = str(n)
    if n in dict_a.keys():
        op += dict_a[n]
    else:
        op += "th"
    return op
