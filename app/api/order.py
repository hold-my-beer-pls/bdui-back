from fastapi import APIRouter
from typing import Any
from app.services.order_service import load_orders, save_order

router = APIRouter()

@router.get("/")
def get_orders():
    return load_orders()

@router.post("/")
def post_order(order: Any):
    return {"orders": save_order(order)}
