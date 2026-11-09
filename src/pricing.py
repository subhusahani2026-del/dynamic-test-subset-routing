def apply_discount(price, discount):
    if discount < 0 or discount > 100:
        raise ValueError("Invalid discount")

    return price - (price * discount / 100)


def add_tax(price):
    return price * 1.18