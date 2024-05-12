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
        text='Попсокет',
        callback_data=LowPriceProduct(
            name='Попсокет',
            price=100,
            lucky_sale=True
        )
    )
    kb.adjust(1)
    return kb.as_markup()

def get_high_price_kb():
    kb = InlineKeyboardBuilder()
    kb.button(
        text='Дорогой попсокет',
        callback_data=HighPriceProduct(
            name='Попсокет',
            price=105
        )
    )
    kb.adjust(1)
    return kb.as_markup()