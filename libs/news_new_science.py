import re

import requests
from aiogram import Bot
from asyncio import sleep
from bs4 import BeautifulSoup

from libs.db import pg_execute, news_is_exist
from config_reader import config


async def get_ns_news(bot: Bot):
    site = "https://new-science.ru"
    url = 'https://new-science.ru/category/iskusstvennyj-intellekt/'
    soup = BeautifulSoup(requests.get(url).text, 'lxml')

    class_filter = re.compile('post-item.*post type-post status-publish.*category-iskusstvennyj-intellekt.*')
    data = soup.find_all('li', class_=class_filter)

    for element in data:
        desc = element.find_all('div', class_='post-details')
        title_div = element.find_all('h2', class_='post-title')

        title = title_div[0].find('a').text
        full_link = site+title_div[0].a['href']
        description = desc[0].find('p').text

        is_exist = await news_is_exist(title=title)
        if not is_exist:
            query = f"INSERT INTO news (title) VALUES ('{title}')"
            await pg_execute(query)

            text = f"<b>{title}</b>\n"
            text += f"\n"
            text += f"{description}\n"
            text += f"\n"
            text += f"{full_link}\n"
            text += f"\n"
            text += f"\n"
            text += f"#from_new_science #added_by_bot"
            await bot.send_message(chat_id=config.channel_id, text=text)
            await sleep(3)

