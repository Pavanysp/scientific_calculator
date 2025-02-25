import math
import pytest
from calculator import square_root, factorial, natural_log, power

# Test for square root function
def test_square_root():
    assert square_root(4) == 2
    assert square_root(9) == 3
    assert round(square_root(2), 5) == round(math.sqrt(2), 5)

# Test for factorial function
def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(1) == 1

# Test for natural log function
def test_natural_log():
    assert round(natural_log(math.e), 5) == 1
    assert round(natural_log(1), 5) == 0

# Test for power function
def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(3, 3) == 27  
