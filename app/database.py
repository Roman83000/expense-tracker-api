import sqlite3


def get_connection():
    return sqlite3.connect('expenses.db', check_same_thread=False)


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

        conn.commit()
        conn.close()

create_tables()