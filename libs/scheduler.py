from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import Bot
from datetime import datetime

from config_reader import config
from libs.news_ria import get_ria_news
from libs.news_it_world import get_it_world_news
from libs.news_new_science import get_ns_news
from asyncio import sleep


async def send_message(bot: Bot):
    # await get_ria_news(bot)
    # await get_it_world_news(bot)
    await get_ns_news(bot)

async def sch(bot: Bot):
    # text = 'some text for test'
    apscheduler = AsyncIOScheduler(timezone="Europe/Moscow")
    apscheduler.add_job(
        send_message,
        trigger='cron',
        start_date=datetime.now(),
        # hour=10,
        # minute=5,
        second='*/5',
        id='send_message',
        kwargs={'bot': bot})
    apscheduler.start()


def test():
    pass