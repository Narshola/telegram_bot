routers = []

from core.handlers.func.func_handler import router
routers.append(router)

from core.handlers.game.game_handler import router
routers.append(router)

from core.handlers.shop_handler import router
routers.append(router)

from core.handlers.contact_handler import router
routers.append(router)

from core.handlers.site.site_handler import router
routers.append(router)

from core.handlers.chat.chat_handler import router
routers.append(router)