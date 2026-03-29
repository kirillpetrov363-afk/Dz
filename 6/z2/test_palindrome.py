import pytest
from palindrome import is_palindrome

def test_palindrome_word():
    assert is_palindrome("КаЗаК") == True

def test_not_palindrome():
    assert is_palindrome("привет") == False

def test_palindrome_with_spaces():
    assert is_palindrome("А роза упала на лапу Азора") == True

def test_palindrome_with_punctuation():
    assert is_palindrome("Лидер бодро, гордо бредил") == True

def test_empty_string():
    assert is_palindrome("") == True

def test_number():
    assert is_palindrome("123321") == True