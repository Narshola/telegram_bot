from aiogram import Dispatcher
from handlers.func.func_handler import *
from handlers.game.game_handler import *


def registration_handlers(dp:Dispatcher):
    func_handler_register(dp)
    game_handler_register(dp)