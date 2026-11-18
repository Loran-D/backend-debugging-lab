orders = [
    {"id": 1, "product": "Laptop", "price": 1200, "quantity": 1, "status":"completed"},
    {"id": 2, "product": "Keyboard", "price": 100, "quantity": 2, "status":"cancelled"},
    {"id": 3, "product": "Mouse", "price": 50, "quantity": 3, "status":"completed"},
]


def get_all_orders():
    return orders


def calculate_total():
    total = 0
    for order in orders:
        if order["status"] == "completed":
            total += order["price"] * order["quantity"]
    return total