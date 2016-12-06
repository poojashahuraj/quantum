import socket
import os
from ConfigParser import NoOptionError
from ConfigParser import RawConfigParser
from TestClasses.set_logging import logging
from TestClasses.get_ftp_connection import TestGetFTPConnection
from TestClasses.ftp_put_test import FtpPutTest
from TestClasses.ftp_put_test import DEFAULT_EXPECT_FAILURE, DEFAULT_BINARY_STORE, DEFAULT_FILE_NAME, \
    DEFAULT_FILE_SIZE_MB
from TestClasses.test_utils import DEFAULT_CFG_DIR
from TestClasses.test_utils import sys_exit


class ConfigFileParser(object):
    """
    This class contains methods and attributes to parse given configuration file.
    """
    def __init__(self, cfg_file_name):
        self.cfg_file_name = cfg_file_name
        self.log = logging.getLogger(__name__)
        self.ftp_connection = None
        self.config = None

    def parse_cfg(self):
        config = RawConfigParser()
        cfg_path = os.path.abspath(os.path.join(DEFAULT_CFG_DIR, self.cfg_file_name))
        config.read(os.path.join(cfg_path))
        self.config = config

        if not self.validate_cfg(cfg_path):
            self.log.error("{} is not valid.".format(cfg_path))
            sys_exit(1)

        # This line assumes each test case section name should start with scenario
        scenario_names = [i for i in self.config.sections() if i.startswith("scenario")]
        test_cases = []
        self.set_ftp_connection()
        # Store each senario as test instace in 'test_cases' list.
        for each_scenario in scenario_names:
            action, info = self.validate_scenario(each_scenario)
            if action == "[put]":
                # Initially set put test case parameters to default values.
                file_name = DEFAULT_FILE_NAME
                file_size_in_mb = DEFAULT_FILE_SIZE_MB
                binary_store = DEFAULT_BINARY_STORE
                expect_failure = DEFAULT_EXPECT_FAILURE
                input_file_path = None

                # In case scenario has parameters specified.
                param_names = self.get_section(each_scenario, "param_names")
                param_values = self.get_section(each_scenario, "param_values")

                # If param_names or param_values field is given in scenario section,
                # then override default values.
                if param_names or param_values:
                    params = self.populate_params(each_scenario, param_names.split(","), param_values.split(","))
                    if "file_name" in params.keys():
                        file_name = params["file_name"]
                    if "expect_failure" in params.keys():
                        expect_failure = params["expect_failure"]
                    if "binary_store" in params.keys():
                        binary_store = params["binary_store"]
                    if "expect_failure" in params.keys():
                        expect_failure = params["expect_failure"]
                    if "input_file_path" in params.keys():
                        input_file_path = params["input_file_path"]
                test = FtpPutTest(each_scenario, info, input_file_path, file_name, file_size_in_mb, binary_store,
                                  expect_failure, self.ftp_connection)
                test_cases.append(test)
        return test_cases

    def set_ftp_connection(self):
        """
        This method reads parameters from setup section in cfg file and stores ftp connection.
        :return:
         boolean : True if ftp_connection is set else system exits.
        """
        user = self.config.get("setup", "user")
        port = self.config.get("setup", "port")
        password = self.config.get("setup", "password")
        hostname = self.config.get("setup", "hostname")
        try:
            self.ftp_connection = TestGetFTPConnection(hostname, port, user, password).get_authentication()
        except socket.error as e:
            self.log.error("Paradise ftp server is not running.")
            sys_exit(1)
        return True

    def validate_cfg(self, cfg_path):
        """
        This method validates if given cfg file has mandatory sections such as set up.
        and number of scenarios is greater than 0.
        :param cfg_path: path of configuration file.
        :return: True if cfg is valid else system exits with error code 1.
        """
        if len(self.config.sections()) == 0:
            self.log.error("No sections found in {}.".format(cfg_path))
            sys_exit(1)

        if "setup" not in self.config.sections():
            self.log.error("Need to have setup section {}.".format(self.cfg_file_name))
            sys_exit(1)
        return True

    def validate_scenario(self, scenario):
        """
        Each scenario in configuration file has to have field info and action.
        :param scenario: string : name of scenario
        :return: action string and info string if everything good, else system exits with error code 1.
        """
        info = self.get_section(scenario, "info")
        action = self.get_section(scenario, "action")
        if not info:
            self.log.error("Each section should have info field, brief descrition of test case.")
            sys_exit(1)
        if not action:
            self.log.error("In scenario section, action field is must.")
            sys_exit(1)
        return action, info

    def populate_params(self, section_name, param_names, param_values):
        """
        This method takes list of parameter names and parameter values, maps them in dictionary.
        :param section_name: string name of section.
        :param param_names: list: list of param names.
        :param param_values: list: list of param values.
        :return: dict : map values of parameter name and value.
        """
        if len(param_names) != len(param_values):
            self.log.error("{} has either param_name or param_value is missing.".format(section_name))
            sys_exit(1)
        params = {}
        for index, value in enumerate(param_names):
            if param_values[index] in ["True", "true", "y", "yes"]:
                param_value = True
            elif param_values[index] in ["false", "False", "n", "no"]:
                param_value = False
            else:
                try:
                    param_value = int(param_values[index])
                except ValueError as e:
                    param_value = param_values[index]
            params[value] = param_value

        return params

    def get_section(self, section, option):
        """
        This method return value of option in given section.
        :param section: str: name of section
        :param option: str : name of option
        :return: str : value of option in given section.
        """
        try:
            value = self.config.get(section, option)
        except NoOptionError as e:
            return None
        return value
