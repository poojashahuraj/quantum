from TestUtils import get_ftp_connection


class UploadFile(object):
    def __init__(self, upload_file_path, ftp_connection=get_ftp_connection(), binary_store=False):
        self._ftp_connection = ftp_connection
        self._upload_file_path = upload_file_path
        self._binary_store = binary_store

    def upload_file(self, ):
        # Open the file
        try:
            upload_file = open(self.upload_file_path, 'r')

            # get the name
            path_split = self.upload_file_path.split('/')
            final_file_name = path_split[len(path_split) - 1]

            if self.binary_store:
                self.ftp_connection.storbinary('STOR ' + final_file_name, upload_file)
            else:
                self.ftp_connection.storlines('STOR ' + final_file_name, upload_file)
            return True
        except IOError:
            print ("No such file or directory... passing to next file")
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