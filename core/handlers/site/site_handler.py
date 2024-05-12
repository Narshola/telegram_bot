from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from core.keyboards.inline.site_inline_keyboards import get_site_inline_keyboard
from core.keyboards.reply.site_reply_keyboards import get_site_reply_keyboard
from core.utils.links import links
from core.utils.texts import welcome, help, about


router = Router(name=__name__)

@router.message(Command(commands=['start']))
async def start_handler(msg:Message):
    await msg.answer(text=welcome, reply_markup=get_site_reply_keyboard())


@router.message(Command(commands=['help']))
async def help_handler(msg:Message):
    await msg.answer(text=help)


@router.message(F.text == "О боте")
async def about_handler(msg:Message):
    await msg.answer(text=about)


@router.message(F.text == "Меню")
async def menu_handler(msg:Message):
    await msg.answer(text=f"Что повторим?", reply_markup=get_site_inline_keyboard())


@router.callback_query()
async def sites_handler(call:CallbackQuery):
    text = ""
    link_list = links[call.data]
    for link in link_list:
        text = text + link[0] + link[1] + "\n"
    await call.message.answer(text=f"{call.data}? Окей, вот полезные сайты:\n{text}")