**ftp_test : Tool to run paradise ftp put tests.**

This project automates PUT tests for paradise FTP server. 
First clone https://github.com/DanKerns/paradise_ftp and start paradise ftp server. 
Confirm paradise ftp server is running before running test cases.

**Build Project:**
1. Clone source code from: https://github.com/poojashahuraj/quantum
2. Build and install package with setup.py. Sample output given below.
```
parallels@ubuntu:~/PycharmProjects/FTPTests$ python setup.py build
running build
running build_scripts
```
```
parallels@ubuntu:~/PycharmProjects/FTPTests$ sudo python setup.py install
running install
running build
running build_scripts
running install_scripts
changing mode of /usr/local/bin/ftp_test to 775
changing mode of /usr/local/bin/ftp_test.py to 755
running install_egg_info
Removing /usr/local/lib/python2.7/dist-packages/ftp_test-1.0.egg-info
Writing /usr/local/lib/python2.7/dist-packages/ftp_test-1.0.egg-info
```
```
parallels@ubuntu:~/PycharmProjects/FTPTests$ ftp_test -h
usage: ftp_test [-h] [--verbose] [--failfast] [-hostname HOSTNAME]
                [-port PORT] [-user USER] [-password PASSWORD]
                [-repeat_times REPEAT_TIMES]

Process arguments for FTP put tests.

optional arguments:
  -h, --help            show this help message and exit
  --verbose             Print logs on terminal.
  --failfast            Exit after first failure.
  -hostname HOSTNAME    Host name of ftp server.
  -port PORT            Port number at which ftp server runs.
  -user USER            Name of the user.
  -password PASSWORD    Password for FTP server.
  -repeat_times REPEAT_TIMES
                        Run tests multiple times.
```

3. Run default test suite.
```
parallels@ubuntu:~/PycharmProjects/quantum$ ftp_test
 2016-12-05 23:53:19,582 INFO in TestRunner.py 19 : Running test suite 1st time.
 2016-12-05 23:53:19,582 INFO in TestRunner.py 21 : --------------------------------------
 2016-12-05 23:53:19,582 INFO in TestRunner.py 22 : Running Test 1
 2016-12-05 23:53:19,582 INFO in TestRunner.py 23 : --------------------------------------
 2016-12-05 23:53:19,582 INFO in TestRunner.py 24 : Default put
 2016-12-05 23:53:19,678 INFO in upload_file.py 29 : Starting 'test_ip.txt' file upload.
 2016-12-05 23:53:19,715 INFO in upload_file.py 31 : OK: Finished uploading test_ip.txt.
 2016-12-05 23:53:19,715 INFO in ftp_put_test.py 58 : Deleting test generated file 'test_ip.txt'.
 2016-12-05 23:53:19,716 INFO in TestRunner.py 21 : --------------------------------------
 2016-12-05 23:53:19,716 INFO in TestRunner.py 22 : Running Test 2
 2016-12-05 23:53:19,716 INFO in TestRunner.py 23 : --------------------------------------
 2016-12-05 23:53:19,716 INFO in TestRunner.py 24 : File name of with 255 characters.
.
.
```
OR you can run test cases defined in configuration file. 
Sample config file here quantum/config_files/put_tests.cfg

```
parallels@ubuntu:~/PycharmProjects/quantum/bin$ ftp_test --cfg_file put_tests.cfg
 2016-12-05 23:54:58,626 INFO in TestRunner.py 19 : Running test suite 1st time.
 2016-12-05 23:54:58,626 INFO in TestRunner.py 21 : --------------------------------------
 2016-12-05 23:54:58,626 INFO in TestRunner.py 22 : Running scenario_1
 2016-12-05 23:54:58,626 INFO in TestRunner.py 23 : --------------------------------------
 2016-12-05 23:54:58,626 INFO in TestRunner.py 24 : Test default put.
 2016-12-05 23:54:58,723 INFO in upload_file.py 29 : Starting 'test_ip.txt' file upload.
 2016-12-05 23:54:58,749 INFO in upload_file.py 31 : OK: Finished uploading test_ip.txt.
 2016-12-05 23:54:58,749 INFO in ftp_put_test.py 58 : Deleting test generated file 'test_ip.txt'.
```

**Adding or Removing test cases**
User can add new test cases in two ways. 
1. Add in python test suite. refer config_files/DefaultTestSuite.py
THis is recommended way to scale up using python. Just need to pass different parameters FtpPutTest.
We can generate custom data files and test it's upload, easy to scale, pythonic way to add parameters.

2. Add in configuration file. refer config_files/put_tests.cfg
This is primitive way of adding test cases, however test are readable for non coders too. Errors in cfg file will be 
caught after running the test suite.
