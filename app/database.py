import sqlite3


def get_connection():
    conn = sqlite3.connect('expenses.db', check_same_thread=False)
    conn.execute('PRAGMA foreign_keys = ON;')
    return conn

def create_tables():
    conn = get_connection()
    c = conn.cursor()
    with conn:
        c.execute("""CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                user_name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                password_hash TEXT NOT NULL
        ) """)

        c.execute("""CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY,
                category TEXT UNIQUE
        ) """)
        
        c.execute("""
        INSERT OR IGNORE INTO categories (category) VALUES
            ('Home'),
            ('Entertainment'),
            ('Transport'),
            ('Food'),
            ('Health');
        """)

        c.execute("""CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY,
                expense_name TEXT NOT NULL,
                amount REAL NOT NULL,
                user_id INTEGER,
                category_id INTEGER,
                CONSTRAINT fk_user_id
                FOREIGN KEY (user_id)
                REFERENCES users(id) ON DELETE CASCADE,
                CONSTRAINT fk_categ_id
                FOREIGN KEY (category_id) 
                REFERENCES categories(id) ON DELETE SET NULL
        )""")
        
# почитати про міграцію баз данних
create_tables()