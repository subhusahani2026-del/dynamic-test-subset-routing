import pytest
from src.pricing import apply_discount, add_tax


def test_apply_discount():
    assert apply_discount(100, 10) == 90


def test_add_tax():
    assert add_tax(100) == 118


def test_invalid_discount():
    with pytest.raises(ValueError):
        apply_discount(100, 120)