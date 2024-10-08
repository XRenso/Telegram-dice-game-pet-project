from loader import dp,bot, set_default_commands
import asyncio
import logging
import sys
from handlers import dice_game, start





async def main():
    dp.include_router(start.router)
    dp.include_router(dice_game.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

    
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())