import sqlite3
from sqlite3 import Connection, Cursor


async def del_all_tags_user(message) -> None:
    chat_id: int = message.chat.id

    connection: Connection = sqlite3.connect("database/send_users.db")
    cursor: Cursor = connection.cursor()

    cursor.execute(
        """UPDATE send_users SET disabled_tags = ? WHERE id = ?""", ("", chat_id)
    )

    connection.commit()

    cursor.close()
    connection.close()
