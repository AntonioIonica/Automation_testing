"""
Abstract class
Test model ABC
"""
from abc import ABC, abstractmethod


class TestModel(ABC):

    @abstractmethod
    def env_setup(self):
        raise NotImplemented
        raise NotImplemented

    @abstractmethod
    def execute_test(self):
        raise NotImplemented

    @abstractmethod
    def close(self):
        raise NotImplemented


