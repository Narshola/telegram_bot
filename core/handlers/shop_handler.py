from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from core.keyboards.inline.shop_keyboards import get_low_price_kb, get_high_price_kb
from core.models.product import LowPriceProduct, HighPriceProduct
from core.middleware.sale_middleware import SaleMiddleware

router = Router(name=__name__)

router.callback_query.middleware(SaleMiddleware())

@router.message(Command(commands=['low_price']))
async def low_price_menu(msg:Message):
    await msg.answer(text='low price menu', reply_markup=get_low_price_kb())

@router.message(Command(commands=['high_price']))
async def high_price_menu(msg:Message):
    await msg.answer(text='high price menu', reply_markup=get_high_price_kb())

@router.callback_query(LowPriceProduct.filter())
async def low_price_callback(call:CallbackQuery, callback_data:LowPriceProduct, is_sale:bool):
    name = callback_data.name
    price = callback_data.get_sale_price(is_sale)
    await call.message.answer(text=f'{name} - отличный выбор! С вас {price} алготокенов!')

@router.callback_query(HighPriceProduct.filter())
async def high_price_callback(call:CallbackQuery, callback_data:HighPriceProduct, is_sale:bool):
    name = callback_data.name
    price = callback_data.get_sale_price(is_sale)
    await call.message.answer(text=f'{name} - отличный выбор! С вас {price} алготокенов!')