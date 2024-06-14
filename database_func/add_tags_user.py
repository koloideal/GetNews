import sqlite3
from sqlite3 import Connection, Cursor


async def update_tags_user(message) -> None:

    chat_id: int = message.chat.id

    connection: Connection = sqlite3.connect('database/send_users.db')
    cursor: Cursor = connection.cursor()

    cursor.execute('SELECT disabled_tags FROM send_users WHERE id = ?', (chat_id,))

    tags_before_update = cursor.fetchone()

    tags_after_update = ' '.join(tags_before_update) + ' ' + message.text.strip()

    cursor.execute('''UPDATE send_users SET disabled_tags = ? WHERE id = ?''', (tags_after_update, chat_id))

    connection.commit()

    cursor.close()
    connection.close()
