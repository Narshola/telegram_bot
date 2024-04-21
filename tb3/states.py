from aiogram.fsm.state import StatesGroup, State


class PlayerRegistrationState(StatesGroup):
    hero_name = State()
    hero_race = State()
    hero_class = State()
    hero_avatar = State()