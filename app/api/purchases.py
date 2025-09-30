from fastapi import APIRouter
from app.services.purchases_service import PurchasesService
from app.models.purchases import UpdateItemModel

router = APIRouter()
service = PurchasesService()

@router.get("")
def get_cart():
    return service.get_cart()

@router.post("/reset")
def reset_cart():
    return service.reset_cart()

@router.delete("/item/{item_id}")
def delete_item(item_id: int):
    return service.delete_item(item_id)

@router.patch("/item/{item_id}")
def update_item(item_id: int, data: UpdateItemModel):
    return service.update_item(item_id, data.dict(exclude_unset=True))
