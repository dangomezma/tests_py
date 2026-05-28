import pytest
from tests_py.pswrd_check.passwort import (is_valid_password,is_over_8,has_caps,has_minuscule,has_no_blanks,has_num)

def test_is_over_8():
    assert is_over_8("Abc12345")
    assert not is_over_8("1234567") 

def test_has_caps():
    assert has_caps("AAbc12345")
    assert not has_caps("1234567")

def test_has_minuscule():
    assert has_minuscule("AAbc12345")
    assert not has_minuscule("1234567") 

def test_has_no_blanks():
    assert has_no_blanks("AAbc12345")
    assert not has_no_blanks("1234 567")

def test_has_num():
    assert has_num("AAbc12345")
    assert not has_num("aaaaaa") 
