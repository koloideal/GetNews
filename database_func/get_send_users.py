import sqlite3
from sqlite3 import Connection, Cursor


async def get_send_users() -> list:

    connection: Connection = sqlite3.connect('database/send_users.db')
    cursor: Cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS send_users 
                     (id INTEGER PRIMARY KEY,
                      is_send blob,
                      disabled_tags varchar(50),
                      UNIQUE(id))''')

    connection.commit()

    cursor.execute('''SELECT id, disabled_tags FROM send_users WHERE is_send''')

    send_users_data: list = []

    for user in cursor.fetchall():

        send_users_data.append({

            'id': user[0],
            'disabled_tags': user[1].split()

        })

    connection.commit()

    cursor.close()
    connection.close()

    return send_users_data
