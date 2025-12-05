import sqlite3
from config import settings

def get_connection():
    conn = sqlite3.connect(settings.DATABASE_URL, check_same_thread=False)
    conn.execute('PRAGMA foreign_keys = ON;')
    try:
        yield conn
    finally:
        conn.close()
