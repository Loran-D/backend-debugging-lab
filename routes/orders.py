from fastapi import APIRouter, HTTPException
from services.order_service import get_all_orders, calculate_total

router = APIRouter()


@router.get("/orders")
def get_orders():
    return get_all_orders()


@router.get("/orders/total")
def get_order_total():
    return {"total": calculate_total()}


@router.get("/orders/{order_id}")
def get_order(order_id: int):
    orders = get_all_orders()

    for order in orders:
        if order["id"] == order_id:
            return order

    raise HTTPException(status_code=404, detail="Order not found")


