import os
from TestUtils import get_ftp_connection, delete_generated_file
from TestClasses.upload_file import UploadFile


class BasicPutTest(object):
    def __init__(self, ftp_connection=get_ftp_connection()):
        self.ftp_conn = ftp_connection

    def put_file(self, input_file_path=None, file_name="test_ip.txt", file_size_in_mb=1, binary_store=False,
                 expect_failure=False):
        test_passed = False
        # 1048576 Bytes = 1 Megabyte
        if not input_file_path:
            try:
                file_size = file_size_in_mb * 1048576
                random_f = open(file_name, "wb")
                random_f.write(os.urandom(file_size))
                random_f.close()
            except IOError as e:
                print e.message
                if expect_failure:
                    return True
                else:
                    return test_passed
            upload_file_path = file_name
        else:
            if not os.path.exists(input_file_path):
                return False
            else:
                upload_file_path = input_file_path

        test_passed = UploadFile(ftp_connection=self.ftp_conn, upload_file_path=upload_file_path,
                                 binary_store=binary_store).upload_file()
        delete_generated_file(upload_file_path)
        return test_passed
