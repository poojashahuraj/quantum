#!/usr/bin/python
import argparse
from Driver.ConfigFileParser import ConfigFileParser
from Driver.TestRunner import TestRunner

parser = argparse.ArgumentParser(description='Process arguments for FTP put tests.')
parser.add_argument('--cfg_file', default='put_tests.cfg', dest="cfg_file", help="name of cfg file where tests "
                                                                                 "are defined.")
parser.add_argument('--verbose', dest='verbose', action='store_true', help="Print logs on terminal.")
parser.add_argument('--failfast', dest='failfast', action='store_true', help="Exit after first failure.")
parser.add_argument('--repeat_times', type=int, dest="repeat_times", default=1, help="Run tests multiple times.")
parser.add_argument('--log_level', type=int, dest="log_level", default=10, choices=[0, 10, 20, 30, 40, 50],
                    help="{0:\"NO_SET\", \"DEBUG\":10, \"INFO\":20, \"WARN\":30, \"ERROR\":40, \"CRITICAL\":50}")

args = parser.parse_args()
test_suite = ConfigFileParser(args.cfg_file).parse_cfg()
TestRunner(test_suite, failfast=args.failfast, repeat_times=args.repeat_times)
