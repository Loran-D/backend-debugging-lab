orders = [
    {"id": 1, "product": "Laptop", "price": 1200, "quantity": 1},
    {"id": 2, "product": "Keyboard", "price": 100, "quantity": 2},
    {"id": 3, "product": "Mouse", "price": 50, "quantity": 3},
]


def get_all_orders():
    return orders


def calculate_total():
    total = sum(order["price"] * order["quantity"] for order in orders)
    return total