import json
from pathlib import Path
from typing import Any

STORAGE_FILE = Path(__file__).parent.parent.parent / "storage/cart.json"
STORAGE_FILE.parent.mkdir(exist_ok=True)

if not STORAGE_FILE.exists():
    STORAGE_FILE.write_text("[]", encoding="utf-8")

def load_cart():
    return json.loads(STORAGE_FILE.read_text(encoding="utf-8"))

def save_cart(data):
    STORAGE_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

def add_item(item: Any):
    cart = load_cart()
    cart.append(item.dict())
    save_cart(cart)
    return cart
