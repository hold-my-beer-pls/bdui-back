from fastapi import APIRouter, Body
from typing import Any
from app.services.cart_service import load_cart, add_item

router = APIRouter()

@router.get("")
def get_cart():
    return load_cart()

@router.post("")
def post_cart(item: Any = Body(...)):
    add_item(item)
    return {"status": 'ok'}
