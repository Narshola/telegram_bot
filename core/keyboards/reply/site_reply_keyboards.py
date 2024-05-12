from aiogram.utils.keyboard import ReplyKeyboardBuilder

def get_site_reply_keyboard():
    keyboard_builder = ReplyKeyboardBuilder()

    keyboard_builder.button(text="Меню")
    keyboard_builder.button(text="О боте")
    keyboard_builder.adjust(1, 2)
    return keyboard_builder.as_markup(
        resize_keyboard=True, 
        one_time_keyboard=True, 
        input_field_placeholder="Нажмите кнопку"
        )