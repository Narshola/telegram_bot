from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault

async def set_commands(bot:Bot):
    commands = [
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
            )
    ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())