from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from database import query


async def cancel_handler(msg:Message, state:FSMContext):
    await msg.answer(text="Команда отменена.")
    await state.clear()


async def show_character(msg:Message):
    data = query('''SELECT * FROM heroes WHERE id=?''', [msg.from_user.id])
    if not data:
        await msg.answer(text="У Вас нет персонажа.\nВы можете его создать, используя команду /form")
    else:
        await msg.answer_photo(photo=data[0][4], caption=f"Ваш персонаж:\n<i>{data[0][2]}-{data[0][3]}</i> по имени <b>{data[0][1]}</b>")


async def delete_character(msg:Message):
    data = query('''SELECT * FROM heroes WHERE id=?''', [msg.from_user.id])
    if not data:
        await msg.answer(text="У Вас нет персонажа.")
    else:
        query('''DELETE FROM heroes WHERE id=?''', [msg.from_user.id])
        await msg.answer(text="Ваш персонаж успешно удалён!")