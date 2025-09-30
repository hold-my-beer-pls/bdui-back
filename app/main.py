from fastapi import FastAPI
from app.api import cart, order, status
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Backend Skeleton")

# Регистрируем роуты
app.include_router(cart.router, prefix="/api/cart", tags=["cart"])
app.include_router(order.router, prefix="/api/order", tags=["order"])
app.include_router(status.router, prefix="/api/status", tags=["status"])
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)