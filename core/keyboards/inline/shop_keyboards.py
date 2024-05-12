from aiogram.utils.keyboard import InlineKeyboardBuilder
from core.models.product import LowPriceProduct, HighPriceProduct

def get_low_price_kb():
    kb = InlineKeyboardBuilder()
    kb.button(
        text='Попсокет',
        callback_data=LowPriceProduct(
            name='Попсокет',
            price=100,
            lucky_sale=True
        )
    )
    kb.button(
        text='Стикер',
        callback_data=LowPriceProduct(
            name='Стикер',
            price=50,
            lucky_sale=True
        )
    )
    kb.adjust(2)
    return kb.as_markup()

def get_high_price_kb():
    kb = InlineKeyboardBuilder()
    kb.button(
        text='Клавиатура',
        callback_data=HighPriceProduct(
            name='Клавиатура',
            price=1000
        )
    )
    kb.button(
        text='Наушники',
        callback_data=HighPriceProduct(
            name='Наушники',
            price=800
        )
    )
    kb.adjust(2)
    return kb.as_markup()