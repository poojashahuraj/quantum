from abc import ABCMeta, abstractmethod


class AbstractTestClass:
    """
    Each test class should be derived from this parent class, hence run_test method will be implemented in each
    test class.
    """
    def __init__(self):
        pass

    __metaclass__ = ABCMeta

    @abstractmethod
    def run_test(self):
        pass
