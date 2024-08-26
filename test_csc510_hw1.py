# For pytest to work, file names should be of the format *_test.py or test_*.py
from csc510_hw1 import add_numbers


def test_addition_correct():
    """Test that the addition function works correctly."""
    assert add_numbers(2, 3) == 5


def test_addition_incorrect():
    """Test that the addition function fails with incorrect data."""
    assert add_numbers(2, 3) == 4
