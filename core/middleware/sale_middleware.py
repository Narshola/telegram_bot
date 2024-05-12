from datetime import datetime
from typing import Callable, Any, Dict, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery

class SaleMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[CallbackQuery, Dict[str, Any]], Awaitable[Any]],
            event: CallbackQuery,
            data: Dict[str, Any]
    ) -> Any:
        hour = datetime.now().time().hour
        data['is_sale'] = 6 > hour >= 0
        result = await handler(event, data)
        return result