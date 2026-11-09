def add_item(cart, item, price):
    cart[item] = price
    return cart


def remove_item(cart, item):
    if item in cart:
        del cart[item]
    return cart


def calculate_total(cart):
    return sum(cart.values())