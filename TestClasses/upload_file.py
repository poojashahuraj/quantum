from test_utils import get_ftp_connection
from TestClasses.set_logging import logging


class UploadFile(object):
    """
    This class contains methods and attributes to upload a file, provided ftp connection is given.
    """
    def __init__(self, upload_file_path, ftp_connection=get_ftp_connection(), binary_store=False):
        self._ftp_connection = ftp_connection
        self._upload_file_path = upload_file_path
        self._binary_store = binary_store
        self.log = logging.getLogger(self.__class__.__name__)

    def upload_file(self, ):
        # Open the file
        try:
            upload_file = open(self.upload_file_path, 'r')

            # get the name
            path_split = self.upload_file_path.split('/')
            final_file_name = path_split[len(path_split) - 1]

            if self.binary_store:
                self.log.info("Starting '{}' file upload in binary format.".format(final_file_name))
                self.ftp_connection.storbinary('STOR ' + final_file_name, upload_file)
                self.log.info("OK: Finished uploading {}.".format(final_file_name))
            else:
                self.log.info("Starting '{}' file upload.".format(final_file_name))
                self.ftp_connection.storlines('STOR ' + final_file_name, upload_file)
                self.log.info("OK: Finished uploading {}.".format(final_file_name))
            return True
        except IOError:
            self.log.error("No such file or directory.".format(self.upload_file_path))
        return False

    @property
    def binary_store(self):
        return self._binary_store

    @binary_store.setter
    def binary_store(self, binary_store):
        self._binary_store = binary_store

    @property
    def ftp_connection(self):
        return self._ftp_connection

    @ftp_connection.setter
    def ftp_connection(self, ftp_connection):
        self._ftp_connection = ftp_connection

    @property
    def upload_file_path(self):
        return self._upload_file_path

    @upload_file_path.setter
    def upload_file_path(self, upload_file_path):
        self._upload_file_path = upload_file_path
