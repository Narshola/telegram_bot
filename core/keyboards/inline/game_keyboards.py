from aiogram.utils.keyboard import InlineKeyboardBuilder
from random import randint


race_list = [
    ["Человек 👨", "человек"], 
    ["Эльф 🧝‍♂️", "эльф"], 
    ["Тёмный эльф 🧛‍♂️", "тёмный эльф"], 
    ["Тролль 🧌", "тролль"], 
    ["Орк 👹", "орк"], 
    ["Гном 🧙‍♂️", "гном"],
    ["Дворф 👷‍♂️", "дворф"],
    ["Нежить 🧟‍♂️", "нежить"], 
    ["Киборг 🦾", "киборг"]
]

class_list = [
    ["Воин 🪓", "воин"],
    ["Паладин 🛡️⚔️", "паладин"],
    ["Жрец ✨", "жрец"],
    ["Ассасин 🗡", "ассасин"],
    ["Маг 🪄", "маг"],
    ["Друид 🍃", "друид"],
    ["Некромант 💀", "некромант"],
    ["Чернокнижник 🔥", "чернокнижник"],
    ["Механик ⚙️", "механик"]
]


def race_inline_keyboard():
    kb = InlineKeyboardBuilder()
    for race in race_list:
        kb.button(text=race[0], callback_data=race[1])
    kb.button(text="Случайная раса! ❓", callback_data=race_list[randint(0, 8)][1])
    kb.adjust(2,2,2,2,2)
    return kb.as_markup()


def class_inline_keyboard():
    kb = InlineKeyboardBuilder()
    for _class in class_list:
        kb.button(text=_class[0], callback_data=_class[1])
    kb.button(text="Случайный класс! ❓", callback_data=class_list[randint(0, 8)][1])
    kb.adjust(2,2,2,2,2)
    return kb.as_markup()