from random import random
from aiogram.filters.callback_data import CallbackData


class LowPriceProduct(CallbackData, prefix='low'):
    name: str
    price: int
    lucky_sale: bool
    def get_sale_price(self, is_sale):
        if is_sale:
            if self.lucky_sale:
                return round(self.price * random())
            return self.price * 0.6
        return self.price
    
class HighPriceProduct(CallbackData, prefix='high'):
    name: str
    price: int
    def get_sale_price(self, is_sale):
        if is_sale:
            return round(self.price * 0.7)
        return self.price