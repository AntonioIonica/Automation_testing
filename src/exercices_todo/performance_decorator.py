"""
performance decorator which calculates how many seconds took for the function to run
"""

from time import time

def performance(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'It took {t2-t1} seconds to run!')
        return result
    return wrapper

@performance
def long_time():
    for i in range(12313231):
        i * 4

long_time()