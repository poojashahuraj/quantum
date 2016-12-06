import logging
import sys
from TestClasses.test_utils import get_str


class TestRunner(object):
    """
    This class contain methods and attributes to run given each test from given list 'tests'.
    """
    def __init__(self, test_suite, failfast=False, repeat_times=1):
        self.test_suite = test_suite
        self.failfast = failfast
        self.repeat_times = repeat_times
        self.log = logging.getLogger(self.__class__.__name__)
        self.run_test()

    def run_test(self):
        for i in range(1, self.repeat_times+1):
            self.log.info("Running test suite {} time.".format(get_str(i)))
            for test in self.test_suite:
                self.log.info("--------------------------------------")
                self.log.info("Running {}".format(test.scenario_name))
                self.log.info("--------------------------------------")
                self.log.info(test.info)
                test_passed = test.run_test()
                if not test_passed:
                    # test failed. if failfast is set to true then exit immediately else continue to next test case.
                    if self.failfast:
                        self.log.error("{} failed.".format(test.scenario_name))
                        sys.exit(1)
                    else:
                        self.log.info("{} failed, still continueing to next test case as failfast is set to False.")
                        continue
            self.log.info("==============================================")
        return 0
