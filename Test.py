import pytest
from main_funcs import (
    get_sq, is_triangle, is_even, get_sq_rect, get_sq_square, city_info
)

def test_get_sq():
    assert get_sq(4.0) == 16.0
    assert get_sq(-3.0) == 9.0

def test_is_triangle():
    assert is_triangle(3, 4, 5)
    assert not is_triangle(1, 2, 3)

def test_is_even():
    assert is_even(2)
    assert not is_even(7)

def test_get_sq_rect():
    assert get_sq_rect(5, 2) == 10
    assert get_sq_rect(0.5, 4) == 2

def test_get_sq_square():
    assert get_sq_square(5) == 25
    assert get_sq_square(1.5) == 2.25

def test_city_info():
    assert city_info("Москва") == ("Москва", 6)
    assert city_info("Питер") == ("Питер", 5)