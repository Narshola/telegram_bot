from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from core.db.database import query, get_data
from core.utils.functions import print_char

router = Router(name=__name__)

@router.message(Command(commands=["cancel"]))
async def cancel_handler(msg:Message, state:FSMContext):
    await msg.answer(text="Команда отменена.")
    await state.clear()


@router.message(Command(commands=["character"]))
async def show_character(msg:Message):
    data = get_data(msg.from_user.id)
    if not data:
        await msg.answer(text="У Вас нет персонажа.\nВы можете его создать, используя команду /form")
    else:
        await msg.answer_photo(photo=data[0][4], caption=print_char("Ваш персонаж", data[0][1], data[0][2], data[0][3]))


@router.message(Command(commands=["delete"]))
async def delete_character(msg:Message):
    data = get_data(msg.from_user.id)
    if not data:
        await msg.answer(text="У Вас нет персонажа.")
    else:
        query('''DELETE FROM heroes WHERE id=?''', [msg.from_user.id])
        await msg.answer(text="Ваш персонаж успешно удалён!")