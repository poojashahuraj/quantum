# coding=utf-8
from TestClasses.ftp_put_test import FtpPutTest
from TestClasses.test_utils import generate_file


class DefaultTestSuite(object):
    def __init__(self, ftp_connection):
        self.ftp_connection = ftp_connection

    def create_test_suite(self):
        test_suite = []
        test_suite.extend([FtpPutTest("Test 1", "Default put", ftp_connection=self.ftp_connection),
                           FtpPutTest("Test 2", "File name of with 255 characters.", file_name="x" * 255,
                                      ftp_connection=self.ftp_connection),
                           FtpPutTest("Test 3", "File name with 256 characters, expect failure.", file_name="x" * 256,
                                      expect_failure=True, ftp_connection=self.ftp_connection),
                           FtpPutTest("Test 4", "Put file of 0 MB size.", file_size_in_mb=0,
                                      ftp_connection=self.ftp_connection),
                           FtpPutTest("Test 5", "Put file of size 5MB", file_size_in_mb=5,
                                      ftp_connection=self.ftp_connection),
                           FtpPutTest("Test 6", "Put file with name \"Ab12@3*&%$\" alphanumeric chars.",
                                      file_name="Ab12@3*&%$", ftp_connection=self.ftp_connection),
                           FtpPutTest("Test 7", "Put file with name \"&%$\", just special characters.",
                                      file_name="&%$", ftp_connection=self.ftp_connection)])

        # If your string is actually a unicode object,
        # you'll need to convert it to a unicode-encoded string object before writing it to a file:
        p = generate_file("unicode_file", u'Δ, Й, ק, ‎ م, ๗, あ, 叶, 葉, and 말.'.encode('utf8'))
        test_suite.extend([FtpPutTest("Test 8", "Put file with unicode data encoded in utf-8.",
                                      input_file_path=p, ftp_connection=self.ftp_connection)])

        # write a file with one char
        p = generate_file("single_char", "8")
        test_suite.append(FtpPutTest("Test 9", "Write a file with just one char.", input_file_path=p,
                                     ftp_connection=self.ftp_connection))

        # Try to upload a file with no data
        p = generate_file("no_data", "")
        test_suite.append(FtpPutTest("Test 10", "Put a file with no data.", input_file_path=p,
                                     ftp_connection=self.ftp_connection))
        return test_suite
