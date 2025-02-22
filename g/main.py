import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.default import Default, DefaultBotProperties
from aiogram.enums import ParseMode
from app.ff import TOKEN
from app_1.handlers import router

async def main():
    bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')



