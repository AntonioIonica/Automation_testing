"""
Test model-abstract class for setUp and tearDown
"""
from abc import ABC, abstractmethod


class TestModel(ABC):

    @abstractmethod
    def setUp(self):
        raise NotImplemented

    @abstractmethod
    def tearDown(self):
        raise NotImplemented
