import pytest

def add(x):
    return x + 1

def subtract(x):
    return x - 1


def test_add():
    assert add(3) == 4

def test_subtract():
    assert subtract(9) == 8