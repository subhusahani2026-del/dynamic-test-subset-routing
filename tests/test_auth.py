from src.auth import authenticate


def test_valid_login():
    assert authenticate("admin", "admin123") is True


def test_invalid_password():
    assert authenticate("admin", "wrong") is False


def test_invalid_user():
    assert authenticate("unknown", "123") is False