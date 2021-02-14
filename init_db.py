import sqlite3

from config import (
    main_user,
    main_pass,
    guest_pass
)

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

insert_query = "INSERT INTO users VALUES (?, ?, ?)"

users = [
    (1, main_user, main_pass),
    (2, 'guest', guest_pass)
]
cursor.executemany(insert_query, users)

connection.commit()
connection.close()
