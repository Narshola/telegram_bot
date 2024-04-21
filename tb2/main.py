#t.me/amseat_bot
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from commands import set_commands
from handler import *
import asyncio


TOKEN = "6713202567:AAFwILU_RCzhUmnIrf2GQumeCT3sYrk5iqo"

async def start():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.startup.register(set_commands)
    dp.message.register(start_handler, Command(commands=['start']))
    dp.message.register(help_handler, Command(commands=['help']))
    dp.message.register(menu_handler, F.text == "Меню")
    dp.message.register(about_handler, F.text == "О боте")
    dp.callback_query.register(sites_handler)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())