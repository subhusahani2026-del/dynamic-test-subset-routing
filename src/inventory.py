inventory = {
    "laptop": 10,
    "phone": 20,
    "headphones": 15
}


def check_stock(item):
    return inventory.get(item, 0)


def update_stock(item, quantity):
    if item not in inventory:
        raise ValueError("Item not found")

    if inventory[item] + quantity < 0:
        raise ValueError("Insufficient stock")

    inventory[item] += quantity
    return inventory[item]