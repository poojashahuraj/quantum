import socket
from ftplib import FTP
import sys
from TestClasses.test_utils import get_pid
from test_utils import DEFAULT_HOSTNAME, DEFAULT_PORT, DEFAULT_USER, DEFAULT_PASSWORD, WELCOME_TXT, PROCESS_NAME
from test_utils import sys_exit
from set_logging import logging


class TestGetFTPConnection(object):
    """
    This class contains methods and attributes to get paradise ftp server's connection.
    """
    def __init__(self, hostname=DEFAULT_HOSTNAME, port=DEFAULT_PORT, user=DEFAULT_USER, password=DEFAULT_PASSWORD):
        self._hostname = hostname
        self._user = user
        self._password = password
        self._port = port
        self.log = logging.getLogger(__name__)

    def get_authentication(self):
        # Get server connection.
        ftp = FTP()
        try:
            ftp.connect(self.hostname, self.port)
            ftp.login(self.user, self.password)
        except socket.error as e:
            self.log.error(e.message)
            self.log.error("Unable to connect to host {}, user {} at port {}.".format(self.hostname, self.user, self.port))
        if not ftp.welcome == WELCOME_TXT:
            self.log.error("Got welcome msg as {}. Should be {}.".format(ftp.welcome, WELCOME_TXT))
            sys_exit(1)
        elif get_pid(PROCESS_NAME) == -1:
            self.log.error("Paradise ftp server is not running. Start paradise ftp server with ./paradise_ftp.")
            sys_exit(1)
        return ftp

    @property
    def hostname(self):
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        self._hostname = hostname

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, port):
        self._port = port

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, user):
        self._user = user

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password