class TestCloseFTPConnection(object):
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
