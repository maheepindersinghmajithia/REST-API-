import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE useders1 (id int, username text, password text)"
cursor.execute(create_table)

user = (1, 'jose', 'asdf')
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

userss = [
    (2, 'josse', 'akksdf'),
    (3, 'anne', 'xyz')
]
cursor.executemany(insert_query, userss)

select_query = "SELECT * FROM useders1"

connection.commit()

connection.close()