import os

from TestClasses.abstract_test_class import AbstractTestClass
from TestClasses.upload_file import UploadFile
from TestClasses.set_logging import logging
from test_utils import get_ftp_connection, delete_generated_file

DEFAULT_FILE_NAME = "test_ip.txt"
DEFAULT_FILE_SIZE_MB = 1
DEFAULT_BINARY_STORE = False
DEFAULT_EXPECT_FAILURE = False


class FtpPutTest(AbstractTestClass):
    """
    This class contains methods and attributes to tests paradise ftp's put functionality.
    """

    def __init__(self, scenario_name, info, input_file_path=None, file_name=DEFAULT_FILE_NAME,
                 file_size_in_mb=DEFAULT_FILE_SIZE_MB, binary_store=DEFAULT_BINARY_STORE,
                 expect_failure=DEFAULT_EXPECT_FAILURE, ftp_connection=get_ftp_connection()):
        super(FtpPutTest, self).__init__()
        self.scenario_name = scenario_name
        self.info = info
        self.ftp_conn = ftp_connection
        self.input_file_path = input_file_path
        self.file_name = file_name
        self.file_size_in_mb = file_size_in_mb
        self.binary_store = binary_store
        self.expect_failure = expect_failure
        self.log = logging.getLogger(self.__class__.__name__)

    def run_test(self):
        test_passed = False
        # 1048576 Bytes = 1 Megabyte
        if not self.input_file_path:
            try:
                file_size = self.file_size_in_mb * 1048576
                random_f = open(self.file_name, "wb")
                random_f.write(os.urandom(file_size))
                random_f.close()
            except IOError as e:
                self.log.warn(e.message)
                if self.expect_failure:
                    return True
                else:
                    return test_passed
            upload_file_path = self.file_name
        else:
            if not os.path.exists(self.input_file_path):
                self.log.error("{} path does not exists.".format(self.input_file_path))
                return False
            else:
                upload_file_path = self.input_file_path

        test_passed = UploadFile(ftp_connection=self.ftp_conn, upload_file_path=upload_file_path,
                                 binary_store=self.binary_store).upload_file()
        self.log.info("Deleting test generated file '{}'.".format(upload_file_path))
        delete_generated_file(upload_file_path)
        return test_passed
