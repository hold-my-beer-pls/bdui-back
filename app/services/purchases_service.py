from copy import deepcopy
from app.data.purchases_data import cart_data, default_cart

class PurchasesService:
    def __init__(self):
        self.cart = deepcopy(cart_data)

    def get_cart(self):
        return self.cart

    def reset_cart(self):
        self.cart = deepcopy(default_cart)
        return self.cart

    def delete_item(self, item_id: int):
        for store in self.cart['stores']:
            store['items'] = [i for i in store['items'] if i['id'] != item_id]
        # Удаляем пустые магазины
        self.cart['stores'] = [store for store in self.cart['stores'] if store['items']]
        self._update_summary()
        return self.cart

    def update_item(self, item_id: int, data: dict):
        for store in self.cart['stores']:
            for item in store['items']:
                if item['id'] == item_id:
                    if 'qty' in data and data['qty'] is not None:
                        item['qty'] = max(1, data['qty'])  # минимальное количество = 1
                    if 'selected' in data and data['selected'] is not None:
                        item['selected'] = data['selected']
                    if 'liked' in data and data['liked'] is not None:
                        item['liked'] = data['liked']
        # Удаляем пустые магазины
        self.cart['stores'] = [store for store in self.cart['stores'] if store['items']]
        self._update_summary()
        return self.cart

    def _update_summary(self):
        # Подсчёт только selected товаров
        total_items = sum(
            item['qty'] for store in self.cart['stores'] for item in store['items'] if item['selected']
        )
        total_price = sum(
            item['qty'] * item['price'] for store in self.cart['stores'] for item in store['items'] if item['selected']
        )
        self.cart['summary']['totalItems'] = total_items
        self.cart['summary']['totalPrice'] = total_price
