from services.order_service import get_all_orders, calculate_total
from fastapi.testclient import TestClient
from main import app

def test_get_all_orders():
    orders = get_all_orders()

    assert len(orders) == 3
    assert orders[0]["product"] == "Laptop"


def test_calculate_total():
    total = calculate_total()

    assert total == 1550



client = TestClient(app)


def test_get_missing_order_returns_404():
    response = client.get("/orders/99")

    assert response.status_code == 404
    assert response.json() == {"detail": "Order not found"}