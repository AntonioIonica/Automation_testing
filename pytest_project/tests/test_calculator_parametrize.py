"""
working up with pytest decorators by parametrizing a func (calculator)
"""
import pytest

products = [
    (2, 3, 6),
    (4, 4, 16),
    (1, 100, 100),
    (10, 2, 20)
]


@pytest.mark.parametrize('a, b, product', products)
def test_multiplication(a, b, product):
    assert a * b == product
