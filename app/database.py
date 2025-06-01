import sqlite3


def get_connection():
    conn = sqlite3.connect('expenses.db', check_same_thread=False)
    return conn

def create_tables():
    conn = get_connection()
    c = conn.cursor()
    with conn:
        c.execute("""CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                user_name TEXT NOT NULL
        ) """)

        c.execute("""CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY,
                expense_name TEXT NOT NULL,
                amount REAL NOT NULL,
                user_id INTEGER,
                CONSTRAINT fk_user_id
                FOREIGN KEY (user_id)
                REFERENCES users(id)
        )""")

create_tables()