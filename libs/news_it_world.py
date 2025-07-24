import requests
from aiogram import Bot
from asyncio import sleep
from bs4 import BeautifulSoup

from libs.db import pg_execute, news_is_exist
from config_reader import config


async def get_it_world_news(bot: Bot):
    site = "https://www.it-world.ru"
    url = 'https://www.it-world.ru/tag/ai/'
    soup = BeautifulSoup(requests.get(url).text, 'lxml')

    data = soup.find_all('div', class_='news-list news-list--img')
    for element in data:
        link = element.find_all('div', class_='news-list__text')
        title_div = element.find_all('div', class_='news-list__title')

        title = title_div[0].find('a').text
        full_link = site+link[0].a['href']
        description = link[0].find('a').text
        # print(title)
        # print(full_link)
        # print(description)

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
            text += f"#from_it_world #added_by_bot"
            await bot.send_message(chat_id=config.channel_id, text=text)
            await sleep(3)

