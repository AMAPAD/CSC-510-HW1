#for pytest to work, file names should be of the format *_test.py or test_*.py
import pytest 
from csc510_hw1 import add 

def test_passing(): #for pytest to work, function names should be of the format test_*.py
    assert add(2, 3)==5 
    
def test_failing(): #for pytest to work, function names should be of the format test_*.py
    assert add(2, 3) == 4
    #pass