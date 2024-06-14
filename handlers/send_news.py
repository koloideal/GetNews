from database_func.get_send_users import get_send_users
from get_data_news.get_news_func import get_news_ixbt
from aiogram.exceptions import TelegramForbiddenError
import logging


async def send_news():

    logging.critical(f'CYCLE NOW')

    from main import bot

    all_need_data_about_users = await get_send_users()
    all_news = await get_news_ixbt()

    for user in all_need_data_about_users:

        user_tags = [x.lower() for x in user['disabled_tags']]

        for news in all_news:

            news_tags = [x.lower() for x in news['tags']]

            if len(set(news_tags).intersection(set(user_tags))) == 0:

                try:

                    await bot.send_message(chat_id=int(user['id']), text=f'{news['title']}\n{news['url']}')

                except TelegramForbiddenError:

                    continue

            else:

                continue
