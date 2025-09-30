# app/models/purchases.py
from pydantic import BaseModel
from typing import Optional

class UpdateItemModel(BaseModel):
    qty: Optional[int] = None
    selected: Optional[bool] = None
    liked: Optional[bool] = None
