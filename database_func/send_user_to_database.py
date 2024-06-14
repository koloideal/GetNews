import sqlite3
from sqlite3 import Connection, Cursor
from aiogram import types


async def send_user_to_database(message: types.Message) -> None:

    chat_id: int = message.chat.id

    connection: Connection = sqlite3.connect('database/send_users.db')
    cursor: Cursor = connection.cursor()

    cursor.execute('''SELECT id FROM send_users WHERE id = ?''', (chat_id,))
    is_in_database = bool(cursor.fetchone())

    connection.commit()

    if is_in_database:

        pass

    else:

        cursor.execute('''INSERT INTO send_users (id, is_send, disabled_tags) VALUES(?, ?, ?)''', (chat_id, False, ''))

    connection.commit()

    cursor.close()
    connection.close()
