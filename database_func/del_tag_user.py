import sqlite3
from sqlite3 import Connection, Cursor


async def del_tags_user(message) -> None | int:
    chat_id: int = message.chat.id

    connection: Connection = sqlite3.connect("database/send_users.db")
    cursor: Cursor = connection.cursor()

    cursor.execute("SELECT disabled_tags FROM send_users WHERE id = ?", (chat_id,))

    tags_before_update = cursor.fetchone()[0].split()

    if message.text.strip() not in tags_before_update:
        return 1

    else:
        tags_after_update = tags_before_update.copy()
        tags_after_update.remove(message.text.strip())

        cursor.execute(
            """UPDATE send_users SET disabled_tags = ? WHERE id = ?""",
            (" ".join(tags_after_update), chat_id),
        )

        connection.commit()

        cursor.close()
        connection.close()
