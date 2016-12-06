from TestClasses.get_ftp_connection import TestGetFTPConnection


class TestSetUp(object):
    """
    This class contains methods and attributes to set up tests, returns ftp connection.
    """
    def __init__(self, hostname, user, password, port):
        self._hostname = hostname
        self._user = user
        self._password = password
        self._port = port

    def setup_test(self):
        ftp = TestGetFTPConnection(hostname=self.hostname,
                                   user=self.user,
                                   port=self.port,
                                   password=self.password).get_authentication()

        return ftp

    @property
    def hostname(self):
        return self._hostname

    @property
    def user(self):
        return self._user

    @property
    def password(self):
        return self._password

    @property
    def port(self):
        return self._port

    @hostname.setter
    def hostname(self, hostname):
        self._hostname = hostname

    @password.setter
    def password(self, password):
        self._password = password

    @user.setter
    def user(self, user):
        self._user = user

    @port.setter
    def port(self, port):
        self._port = port
