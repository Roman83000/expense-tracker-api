-- UP: Створення початкових таблиць users та expenses (без категорій)

CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    user_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE, -- when move to "real" db use case insensitive type for email
    password_hash TEXT NOT NULL
);

CREATE TABLE expenses (
    id INTEGER PRIMARY KEY,
    expense_name TEXT NOT NULL,
    amount INTEGER NOT NULL,
    user_id INTEGER,
    CONSTRAINT fk_user_id
    FOREIGN KEY (user_id)
    REFERENCES users(id) ON DELETE CASCADE
);