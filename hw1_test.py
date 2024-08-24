import pytest 
from hw1 import add 

def test_passing(): 
    assert add(2, 3)==5 
    
def test_failing(): 
    #assert add(2, "3") == 4
    pass