# Tests

import pytest
from app import add, subtract

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 3) == -3

# To demonstrate a failing test (optional)
def test_fail():
    assert subtract(2, 2) == 3  # This will fail
