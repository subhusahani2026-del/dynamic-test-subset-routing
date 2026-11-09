import pytest
from src.inventory import check_stock, update_stock


def test_check_stock():
    assert check_stock("laptop") == 10


def test_update_stock():
    assert update_stock("laptop", 5) == 15


def test_invalid_stock():
    with pytest.raises(ValueError):
        update_stock("unknown", 5)