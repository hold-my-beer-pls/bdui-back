import json
from pathlib import Path
from typing import Any

STORAGE_FILE = Path(__file__).parent.parent.parent / "storage/order.json"
STORAGE_FILE.parent.mkdir(exist_ok=True)

if not STORAGE_FILE.exists():
    STORAGE_FILE.write_text("[]", encoding="utf-8")

def load_orders():
    return json.loads(STORAGE_FILE.read_text(encoding="utf-8"))

def save_order(order: Any):
    orders = load_orders()
    orders.append(order.dict())
    STORAGE_FILE.write_text(json.dumps(orders, ensure_ascii=False, indent=2), encoding="utf-8")
    return orders
