#t.me/amseat_bot
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from my_first_handler import *
import asyncio


TOKEN = "6713202567:AAFwILU_RCzhUmnIrf2GQumeCT3sYrk5iqo"

async def start():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    # dp.message.register(my_first_handler)
    dp.message.register(hello_handler, (F.text=="Привет") | (F.text=="Добрый день"))
    dp.message.register(goodbye_handler, (F.text.startswith("Пока")) & (F.text.endswith("!")))
    dp.message.register(caps_handler, F.text.isupper())
    dp.message.register(photo_handler, F.photo)
    dp.message.register(voice_handler, F.voice)
    dp.message.register(video_handler, F.video)
    dp.message.register(sticker_handler, F.sticker)
    dp.message.register(summ_handler, F.text.startswith("Сложи"))
    dp.message.register(error_handler)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())