import psutil


def performance_testing(**test_type):
    def inner(func):
        def wrapper(expected):
            if test_type['name'] == 'memory':
                actual_data = psutil.virtual_memory().percent
                if expected - 10 <= actual_data <= expected + 10:
                    print(f'Test passed, actual result being {actual_data}')
                else:
                    print('Test failed')
            elif test_type['name'] == 'cpu':
                if psutil.cpu_percent() == expected:
                    print('Test passed')
                else:
                    print('Test failed')
            func(expected)

        return wrapper

    return inner


@performance_testing(name='memory')
def test_search_performance(expected):
    print(f'Expected value is {expected}')


test_search_performance(60.9)

#TODO de incercat alt parametru, sa schimbam un atribut si sa migram catre celalalt exercitiu
