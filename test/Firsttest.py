import pytest

def add(x):
    return x + 1

def subtract(x):
    return x - 1

def multiply(x,y):
    return x * y


def test_add():
    assert add(3) == 4

def test_subtract():
    assert subtract(9) == 8

def test_multiply():
    assert multiply(3,4) == 12