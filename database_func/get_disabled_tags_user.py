import sqlite3
from sqlite3 import Connection, Cursor


async def get_disabled_tags_user(chat_id) -> list:

    connection: Connection = sqlite3.connect('database/send_users.db')
    cursor: Cursor = connection.cursor()

    cursor.execute('''SELECT disabled_tags FROM send_users WHERE id = ?''', (chat_id, ))

    disabled_tags_user: list = cursor.fetchone()[0].split()

    connection.commit()

    cursor.close()
    connection.close()

    return disabled_tags_user
