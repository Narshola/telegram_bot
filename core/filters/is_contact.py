from aiogram.filters import BaseFilter
from aiogram.types import Message

class IsTrueContact(BaseFilter):
    async def __call__(self, msg:Message) -> bool:
        return msg.contact.user_id == msg.from_user.id