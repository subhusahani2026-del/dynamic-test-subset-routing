from src.cart import add_item, remove_item, calculate_total


def test_add_item():
    cart = {}
    add_item(cart, "Laptop", 50000)
    assert cart["Laptop"] == 50000


def test_remove_item():
    cart = {"Phone": 20000}
    remove_item(cart, "Phone")
    assert "Phone" not in cart


def test_calculate_total():
    cart = {"Laptop": 50000, "Phone": 20000}
    assert calculate_total(cart) == 70000