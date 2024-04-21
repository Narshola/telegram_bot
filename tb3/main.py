#t.me/amseat_bot
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from commands import set_commands
from func_handler import *
from game_handler import *
from states import PlayerRegistrationState as PRS
import asyncio


TOKEN = "6713202567:AAFwILU_RCzhUmnIrf2GQumeCT3sYrk5iqo"

async def start():
    bot = Bot(token=TOKEN, parse_mode="HTML")
    dp = Dispatcher()
    
    dp.startup.register(set_commands)

    dp.message.register(cancel_handler, Command(commands=["cancel"]))

    dp.message.register(get_form_handler, Command(commands=["form"]))
    dp.message.register(get_name_handler, PRS.hero_name)
    dp.callback_query.register(get_race_handler, PRS.hero_race)
    dp.callback_query.register(get_class_handler, PRS.hero_class)
    dp.message.register(get_avatar_handler, PRS.hero_avatar)
    dp.message.register(show_character, Command(commands=["character"]))
    dp.message.register(delete_character, Command(commands=["delete"]))
    
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())