from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault

async def set_commands(bot:Bot):
    commands = [
        BotCommand(
            command='start',
            description='Начало работы'
        ),
        BotCommand(
            command='help',
            description='Помощь'
        ),
        BotCommand(
            command="form",
            description="Создать персонажа"
        ),
        BotCommand(
            command="character",
            description="Посмотреть персонажа"
        ),
        BotCommand(
            command="delete",
            description="Удалить персонажа"
        ),
        BotCommand(
            command="cancel",
            description="Отменить команду"
            ),
        BotCommand(
            command="low_price",
            description="Товары по низким ценам"
        ),
        BotCommand(
            command="high_price",
            description="Товары по высоким ценам"
        )
    ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())