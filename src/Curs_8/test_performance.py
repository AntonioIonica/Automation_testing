"""
Test performance class
"""
from src.Curs_8.recap_ABC import TestModel
import psutil


class TestPerf(TestModel):

    def env_setup(self):
        pass

    def execute_test(self):
        vm = psutil.virtual_memory().percent
        cpu = psutil.cpu_percent()
        print(f'Your virtual memory is {vm}')

    def close(self):
        pass


if __name__ == '__main__':
    repo = TestPerf()
    repo.execute_test()
