import pytest 
from hw1 import add 

def passing_test(): #for pytest to work, function names and file names should be of the format *_test.py or test_*.py
    assert add(2, 3)==5 
    
def failing_test(): #for pytest to work, function names and file names should be of the format *_test.py or test_*.py
    assert add(2, "3") == 4
    #pass