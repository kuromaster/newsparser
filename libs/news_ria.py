import requests
from aiogram import Bot
from asyncio import sleep
from bs4 import BeautifulSoup

from libs.db import pg_execute, news_is_exist
from config_reader import config


url = 'https://ria.ru/product_iskusstvennyy-intellekt/'
# page = requests.get(url)
# tree = html.fromstring(page.content)
# titles = tree.xpath('//div[contains(@class,"list-item__content")')


async def get_ria_news(bot: Bot):
    soup = BeautifulSoup(requests.get(url).text, 'lxml')

    titles = soup.find_all('div', class_='list-item__content')
    for title in titles:

        is_exist = await news_is_exist(title=title.text)
        if not is_exist:
            query = f"INSERT INTO news (title) VALUES ('{title.text}')"
            await pg_execute(query)

            text = f"<b>{title.text}</b>\n"
            text += f"{title.find('a')['href']}\n"
            text += f"\n"
            text += f"\n"
            text += f"#from_ria #added_by_bot"
            await bot.send_message(chat_id=config.channel_id, text=text)
            await sleep(3)

# for title in titles:
# print(title.text)
# print(title)
# print(title.find('a')['href'])
