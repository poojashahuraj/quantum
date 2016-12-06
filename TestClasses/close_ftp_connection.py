class TestCloseFTPConnection(object):
    """
    This class contains method and attributes to close the ftp connection. Even though its not explicitly needed.
    """
    def __init__(self, session):
        self._session = session

    def close_session(self):
        self.session.close()

    @property
    def session(self):
        return self._session

    @session.setter
    def session(self, session):
        self._session = session
