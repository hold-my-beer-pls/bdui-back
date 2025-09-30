default_cart = {
    "stores": [
        {
            "id": 1,
            "name": "Pear Store",
            "rating": 4.8,
            "reviews": 643,
            "items": [
                {
                    "id": 101,
                    "title": "Зарядка MagSafe Charger 15W 1 метр",
                    "price": 9481,
                    "qty": 2,
                    "image": "magsafe.png",
                    "liked": False,
                    "selected": True
                },
                {
                    "id": 102,
                    "title": "AirPods Pro 2",
                    "price": 15990,
                    "qty": 1,
                    "image": "airpods.png",
                    "liked": True,
                    "selected": True
                }
            ]
        },
        {
            "id": 2,
            "name": "TECHNO ZONE",
            "rating": 5.0,
            "reviews": 916,
            "items": [
                {
                    "id": 201,
                    "title": "iPhone 16 Pro, 256 ГБ",
                    "price": 99990,
                    "qty": 1,
                    "image": "iphone.png",
                    "liked": False,
                    "selected": True
                }
            ]
        }
    ],
    "promotions": [
        {
            "id": 301,
            "title": "Apple Watch 10 42mm Blue",
            "price": 26591,
            "oldPrice": 27990,
            "discount": 5,
            "image": "apple-watch.png",
            "storeId": 1
        }
    ],
    "summary": {
        "totalItems": 3,
        "totalPrice": 109471,
        "currency": "₽"
    }
}

# Этот объект будем клонировать при ресете
cart_data = default_cart.copy()
