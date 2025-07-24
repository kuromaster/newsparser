# -*- coding: utf-8 -*-


import logging
import traceback
import asyncio
from datetime import datetime
from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from config_reader import config
from libs.tools import seconds_count
from libs.scheduler import sch
from libs.db import init_db
from middleware.scheduler_mw import SchedulerMiddleware

from handlers import getid_h


time_start = datetime.now()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s",
    # filename="logs/mednotebot.log",
    # filemode="w"
)

logger = logging.getLogger(__name__)


async def on_startup(bot: Bot ):
    # logger.info("Запуск бота...")
    await seconds_count(logger, time_start, "Запуск бота..")
    await sch(bot)


async def on_shutdown():
    logger.info("Выключение бота...")


async def main():
    # scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
    try:
        # проверяем и если нет, то создаём нужные таблицы в БД
        await init_db()

        # иницилизируем бота
        bot = Bot(token=config.bot_token.get_secret_value(), default=DefaultBotProperties(parse_mode=ParseMode.HTML))

        # await bot.send_message(config.channel_id, "Бот парсер запущен")
        # Диспетчер handlers
        dp = Dispatcher()

        # Регистрация scheduler middleware в диспетчере
        # dp.update.middleware.register(SchedulerMiddleware(scheduler))

        # Добавляем роуты в диспетчер
        dp.include_routers(getid_h.router)
        # dp.include_routers(menu_h.router)
        # dp.include_routers(gpt_h.router)

        await seconds_count(logger, time_start, "Добавлены все handler-ы")

        # Register
        dp.startup.register(on_startup)
        dp.shutdown.register(on_shutdown)
        await seconds_count(logger, time_start, "Зарегистрированы события on_start и on_shutdown")

        # Не обрабатывать сообщение в ТГ присланные пока бот не работал
        await bot.delete_webhook(drop_pending_updates=True)
        await seconds_count(logger, time_start, "Объявлено, о пропуске новых updates во время простоя бота")

        # Запуск бота
        await dp.start_polling(bot)

    except Exception as e:
        logger.error('====================================================')
        logger.error(e)
        logger.error('====================================================')
        logger.error(traceback.format_exc())
        logger.error('====================================================')
    finally:
        logger.info('[finally] Выключение бота')


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Работа бота завершена. Статус -- выключен")
