import sqlite3
from sqlite3 import Connection, Cursor
from aiogram import types


async def add_send_user(message: types.Message) -> None:

    chat_id: int = message.chat.id

    connection: Connection = sqlite3.connect('database/send_users.db')
    cursor: Cursor = connection.cursor()

    cursor.execute('''UPDATE send_users SET is_send = ? WHERE id = ?''', (True, chat_id))

    connection.commit()

    cursor.close()
    connection.close()
