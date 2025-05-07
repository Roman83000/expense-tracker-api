import sqlite3

conn = sqlite3.connect('expenses.db')

c = conn.cursor()

# запит нижче виконав
# c.execute("""CREATE TABLE users (
#           id INTEGER PRIMARY KEY,
#           user_name TEXT NOT NULL
# ) """)

# запит нижче виконав
# c.execute("""CREATE TABLE expenses (
#           id INTEGER PRIMARY KEY,
#           expense_name TEXT NOT NULL,
#           amount REAL NOT NULL,
#           user_id INTEGER,
#           CONSTRAINT fk_user_id
#           FOREIGN KEY (user_id)
#           REFERENCES users(id)
#  )""")

conn.commit()

conn.close()