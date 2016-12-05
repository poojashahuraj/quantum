from ftplib import FTP
import sys
from TestClasses.TestUtils import get_pid
from TestUtils import DEFAULT_HOSTNAME, DEFAULT_PORT, DEFAULT_USER, DEFAULT_PASSWORD, WELCOME_TXT, PROCESS_NAME


class TestGetFTPConnection(object):
    def __init__(self, hostname=DEFAULT_HOSTNAME, port=DEFAULT_PORT, user=DEFAULT_USER, password=DEFAULT_PASSWORD):
        self._hostname = hostname
        self._user = user
        self._password = password
        self._port = port

    def get_authentication(self):
        # Get server connection.
        ftp = FTP()
        ftp.connect(self.hostname, self.port)
        ftp.login(self.user, self.password)
        if not ftp.welcome == WELCOME_TXT:
            print "Server connection failed."
            sys.exit(1)
        elif get_pid(PROCESS_NAME) == -1:
            print "paradise ftp server is not running. Start paradise ftp server with ./paradise_ftp."
            sys.exit(1)
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
