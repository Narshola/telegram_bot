from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from states import PlayerRegistrationState as PRS
from game_keyboards import *
from database import insert, query


async def get_form_handler(msg:Message, state:FSMContext):
    data = query('''SELECT * FROM heroes WHERE id=?''', [msg.from_user.id])
    if data:
        await msg.answer_photo(photo=data[0][4], caption=f"У Вас уже есть персонаж:\n{data[0][2]}-{data[0][3]} по имени {data[0][1]}.")
    else:
        await msg.answer(text="Добро пожаловать в форму регистрации.\nВведите имя персонажа")
        await state.update_data(hero_name=msg.text)
        await state.set_state(PRS.hero_name)


async def get_name_handler(msg:Message, state:FSMContext):
    await msg.answer(text=f"Имя персонажа - {msg.text}. Выберите расу", reply_markup=race_inline_keyboard())
    await state.update_data(hero_name=msg.text)
    await state.set_state(PRS.hero_race)


async def get_race_handler(call:CallbackQuery, state:FSMContext):
    await call.message.answer(text=f"Раса персонажа - {call.data}. Выберите класс", reply_markup=class_inline_keyboard())
    await state.update_data(hero_race=call.data)
    await state.set_state(PRS.hero_class)
    await call.answer()


async def get_class_handler(call:CallbackQuery, state:FSMContext):
    await call.message.answer(text=f"Класс персонажа - {call.data}. Загрузите фото персонажа")
    await state.update_data(hero_class=call.data)
    await state.set_state(PRS.hero_avatar)
    await call.answer()


async def get_avatar_handler(msg:Message, state:FSMContext):
    try:
        file = msg.photo[-1].file_id
        await state.update_data(hero_avatar=file)
        data = await state.get_data()
        query(insert, [msg.from_user.id, data['hero_name'], data['hero_race'], data['hero_class'], data['hero_avatar']])
        await msg.answer_photo(photo=data['hero_avatar'], caption=f"Ваш персонаж:\n<i>{data['hero_race']}-{data['hero_class']}</i> по имени <b>{data['hero_name']}</b>")
        await state.clear()  
    except:
        await msg.answer(text="Нет фото. Загрузите фото персонажа:")