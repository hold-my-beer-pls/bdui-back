from fastapi import FastAPI
from app.api import cart, order

app = FastAPI(title="Backend Skeleton")

# Регистрируем роуты
app.include_router(cart.router, prefix="/api/cart", tags=["cart"])
app.include_router(order.router, prefix="/api/order", tags=["order"])
