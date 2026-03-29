import pytest
from average import average_num

def test_simple_integers():
    assert average_num([1, 1]) == 1

def test_floats():
    assert average_num([2.5, 3.5]) == 3

def test_multiple_numbers():
    assert average_num([1, 2, 3]) == 2

def test_single_element():
    assert average_num([10]) == 10

def test_string_numbers():
    assert average_num(["1", "2"]) == 1.5

def test_mixed_types():
    assert average_num([1, "2", 3]) == 2

def test_invalid_string():
    assert average_num([1, "abc", 3]) == "Bad request"

def test_zeros():
    assert average_num([0, 0, 0]) == 0

def test_negative_numbers():
    assert average_num([-1, -2, -3]) == -2

def test_mixed_float_int():
    assert average_num([1, 2.5, 3]) == 2.17