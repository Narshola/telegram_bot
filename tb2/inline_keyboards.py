from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_inline_keyboard():
    keyboard_builder = InlineKeyboardBuilder()

    keyboard_builder.button(text="Python", callback_data="Python")
    keyboard_builder.button(text="C++", callback_data="C++")
    keyboard_builder.button(text="Arduino", callback_data="Arduino")
    keyboard_builder.button(text="SQL", callback_data="SQL")
    keyboard_builder.adjust(2, 2)
    return keyboard_builder.as_markup()