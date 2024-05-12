from aiogram import Router, F
from aiogram.types import Message
from core.filters.is_contact import IsTrueContact


router = Router(name=__name__)

@router.message(F.contact, IsTrueContact)
async def get_true_contact(msg:Message):
    await msg.answer(text='Вы прислали свой контакт')

@router.message(F.contact)
async def get_true_contact(msg:Message):
    await msg.answer(text='Вы прислали не свой контакт')