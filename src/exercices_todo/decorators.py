"""
decorators building
"""

def stars(func):
    def wrapper(*args, **kwargs):
        print('\t\t*************')
        func(*args, **kwargs)
        print('\t\t*************')
    return wrapper

@stars
def greet(message, emoji=':))'):
    print(message, emoji)

greet('Hello')