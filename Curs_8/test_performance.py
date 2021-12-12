"""
Test performance class
"""
import psutil


class TestPerf:

    def env_setup(self):
        pass

    def execute_test(self):
        """

        :return:
        """
        vm = psutil.virtual_memory().percent
        cpu = psutil.cpu_percent()
        print(f'Your virtual memory is {vm}%')
        print(f'Your CPU usage is {cpu}%')

    def close(self):
        pass


if __name__ == '__main__':
    repo = TestPerf()
    repo.execute_test()
