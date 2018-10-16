#conversions.py
import pytest
import math

def absVal(x):
    ''' Return the absolute value of x'''
    return math.sqrt(x**2)
##    if x > 0:
##        return x
##    else:
##        return -1*x

def test_absVal_1():
    assert absVal(1) == 1

def test_absVal_2():
    assert absVal(0) == 0

def test_absVal_3():
    assert absVal(-1) == 1

def test_absVal_4():
    assert absVal(-100) == 100

def test_absVal_5():
    assert absVal(-2) == 2

def test_sqrt():
    assert math.sqrt(2)*math.sqrt(2) == pytest.approx(2)


    

