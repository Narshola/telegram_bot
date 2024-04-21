from aiogram import Bot, Dispatcher
from aiogram.types import Message


# async def my_first_handler(msg:Message, bot:Bot):
#     await bot.send_message(chat_id=msg.from_user.id, text="Hello! I'm bot!")


# async def my_first_handler(msg:Message):
#     await msg.answer(text="Hello! I'm bot!")


# async def my_first_handler(msg:Message):
#     await msg.answer(text=f'{msg.text}')


async def hello_handler(msg:Message):
    await msg.answer(text=f"Привет, {msg.from_user.first_name}!")


async def goodbye_handler(msg:Message):
    await msg.answer(text="Пока!")


async def error_handler(msg:Message):
    await msg.answer(text=f"Мне нечего ответить.")


async def photo_handler(msg:Message):
    await msg.reply(text="Классное фото!")


async def voice_handler(msg:Message):
    await msg.reply(text="У вас приятный голос!")


async def video_handler(msg:Message):
    await msg.reply(text="Какое интересное видео!")


async def sticker_handler(msg:Message):
    await msg.reply(text="Крутой стикер!")


async def summ_handler(msg:Message):
    calc = msg.text.split(" ")
    try:
        value_1 = int(calc[1])
        value_2 = int(calc[3])
    except:
        await msg.answer(text="Введите по шаблону: Сложи <число1> и <число2>")
        return
    await msg.answer(text=f"Сумма: {value_1 + value_2}")


async def caps_handler(msg:Message):
    await msg.answer(text="Не кричите на меня, пожалуйста!")