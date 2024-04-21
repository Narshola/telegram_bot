from aiogram.types import Message, CallbackQuery
from inline_keyboards import get_inline_keyboard
from tb3.reply_keyboards import get_reply_keyboard
from links import links
from texts import *

async def start_handler(msg:Message):
    await msg.answer(text=welcome, reply_markup=get_reply_keyboard())


async def help_handler(msg:Message):
    await msg.answer(text=help)


async def about_handler(msg:Message):
    await msg.answer(text=about)


async def menu_handler(msg:Message):
    await msg.answer(text=f"Что повторим?", reply_markup=get_inline_keyboard())


async def sites_handler(call:CallbackQuery):
    text = ""
    link_list = links[call.data]
    for link in link_list:
        text = text + link[0] + link[1] + "\n"
    await call.message.answer(text=f"{call.data}? Окей, вот полезные сайты:\n{text}")