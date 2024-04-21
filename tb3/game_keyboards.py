from aiogram.utils.keyboard import InlineKeyboardBuilder
from random import randint


race_list = ["человек", "эльф", "тёмный эльф", "тролль", "орк", "гном", "дворф", "нежить", "киборг"]
class_list = ["воин", "паладин", "жрец", "ассасин", "маг", "друид", "некромант", "чернокнижник", "механик"]

def race_inline_keyboard():
    kb = InlineKeyboardBuilder()
    kb.button(text="Человек 👨", callback_data="человек")
    kb.button(text="Эльф 🧝‍♂️", callback_data="эльф")
    kb.button(text="Тёмный эльф 🧛‍♂️", callback_data="тёмный эльф")
    kb.button(text="Тролль 🧌", callback_data="тролль")
    kb.button(text="Орк 👹", callback_data="орк")
    kb.button(text="Гном 🧙‍♂️", callback_data="гном")
    kb.button(text="Дворф 👷‍♂️", callback_data="дворф")
    kb.button(text="Нежить 🧟‍♂️", callback_data="нежить")
    kb.button(text="Киборг 🦾", callback_data="киборг")
    kb.button(text="Случайная раса! ❓", callback_data=race_list[randint(0, 6)])
    kb.adjust(2,2,2,2,2)
    return kb.as_markup()


def class_inline_keyboard():
    kb = InlineKeyboardBuilder()
    kb.button(text="Воин 🪓", callback_data="воин")
    kb.button(text="Паладин 🛡️⚔️", callback_data="паладин")
    kb.button(text="Жрец ✨", callback_data="жрец")
    kb.button(text="Ассасин 🗡", callback_data="ассасин")
    kb.button(text="Маг 🪄", callback_data="маг")
    kb.button(text="Друид 🍃", callback_data="друид")
    kb.button(text="Некромант 💀", callback_data="некромант")
    kb.button(text="Чернокнижник 🔥", callback_data="чернокнижник")
    kb.button(text="Механик ⚙️", callback_data="механик")
    kb.button(text="Случайный класс! ❓", callback_data=class_list[randint(0, 6)])
    kb.adjust(2,2,2,2,2)
    return kb.as_markup()