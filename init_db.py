import sqlite3

from settings.config import (
    main_user,
    main_pass,
    guest_pass
)

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)"
cursor.execute(create_table)

insert_query = "INSERT INTO users VALUES (?, ?, ?)"

defaults = [
    (1, main_user, main_pass),
    (2, 'guest', guest_pass)
]
cursor.executemany(insert_query, defaults)

connection.commit()
connection.close()
