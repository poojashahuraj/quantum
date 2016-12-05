**ftp_test : Tool to run paradise ftp put tests.**

This project automates few PUT tests for paradise FTP server. 
First clone https://github.com/DanKerns/paradise_ftp and start paradise ftp server. 
Confirm paradise ftp server is running before running test cases.

**Build Project:**
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
This will run all tests three times.
```
parallels@ubuntu:~/PycharmProjects/FTPTests$ ftp_test --repeat_times 3
```