# coding=utf-8
import sys
from TestClasses.basic_put_test import BasicPutTest
from TestUtils import generate_file, get_ftp_connection


class RunAllTests(object):
    def __init__(self, ftp_connection):
        self._ftp_connection = ftp_connection

    def run_tests(self):
        if self.ftp_connection is None:
            print "No connection"
            sys.exit(1)

        test = BasicPutTest()
        assert test.put_file() is True
        assert test.put_file(file_name="x" * 255) is True
        assert test.put_file(file_name="x" * 256, expect_failure=True) is True
        assert test.put_file(file_size_in_mb=0) is True
        assert test.put_file(file_size_in_mb=1) is True
        assert test.put_file(file_name="Ab12@3*&%$") is True
        assert test.put_file(file_name="&%$") is True

        # If your string is actually a unicode object,
        # you'll need to convert it to a unicode-encoded string object before writing it to a file:
        p = generate_file("unicode_file", u'Δ, Й, ק, ‎ م, ๗, あ, 叶, 葉, and 말.'.encode('utf8'))
        assert test.put_file(input_file_path=p) is True

        # write a file with one char
        p = generate_file("single_char", "8")
        assert test.put_file(input_file_path=p) is True

        # Try to upload a file with no data
        p = generate_file("no_data", "")
        assert test.put_file(input_file_path=p) is True

    @property
    def ftp_connection(self):
        return self._ftp_connection

    @ftp_connection.setter
    def ftp_connection(self, ftp_connection):
        self._ftp_connection = ftp_connection

if __name__ == "__main__":
    print "hello"
    ftp_conn = get_ftp_connection()
    RunAllTests(ftp_conn).run_tests()