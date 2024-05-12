from aiogram import Router, F
from aiogram.types import Message


router = Router(name=__name__)

@router.message((F.text=="Привет") | (F.text=="Добрый день"))
async def hello_handler(msg:Message):
    await msg.answer(text=f"Привет, {msg.from_user.first_name}!")


@router.message((F.text.startswith("Пока")) & (F.text.endswith("!")))
async def goodbye_handler(msg:Message):
    await msg.answer(text="Пока!")


@router.message(F.photo)
async def photo_handler(msg:Message):
    await msg.reply(text="Классное фото!")


@router.message(F.voice)
async def voice_handler(msg:Message):
    await msg.reply(text="У вас приятный голос!")


@router.message(F.video)
async def video_handler(msg:Message):
    await msg.reply(text="Какое интересное видео!")


@router.message(F.sticker)
async def sticker_handler(msg:Message):
    await msg.reply(text="Крутой стикер!")


@router.message(F.text.startswith("Сложи"))
async def summ_handler(msg:Message):
    calc = msg.text.split(" ")
    try:
        num1 = int(calc[1])
        num2 = int(calc[3])
    except:
        await msg.answer(text="Введите по шаблону: Сложи <число1> и <число2>")
        return
    await msg.answer(text=f"Сумма: {num1 + num2}")


@router.message(F.text.isupper())
async def caps_handler(msg:Message):
    await msg.answer(text="Не кричите на меня, пожалуйста!")


@router.message()
async def error_handler(msg:Message):
    await msg.answer(text=f"Мне нечего ответить.")