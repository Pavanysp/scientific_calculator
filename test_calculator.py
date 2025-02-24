import math
import pytest
from calculator import square_root, factorial, natural_log, power

def test_square_root():
    assert square_root(4) == 2
    assert square_root(9) == 3
    assert round(square_root(2), 5) == round(math.sqrt(2), 5)

def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(1) == 1

def test_natural_log():
    assert round(natural_log(math.e), 5) == 1
    assert round(natural_log(1), 5) == 0

def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(3, 3) == 27
