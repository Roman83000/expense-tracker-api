-- UP: Додає таблицю categories та оновлює таблицю expenses

-- 1. Створення таблиці categories
CREATE TABLE categories (
    id INTEGER PRIMARY KEY,
    category TEXT UNIQUE
);

-- 2. Заповнення таблиці categories початковими даними
INSERT INTO categories (category) VALUES
    ('Home'),
    ('Entertainment'),
    ('Transport'),
    ('Food'),
    ('Health');

-- 3. Оновлення таблиці expenses (перебудова для додавання зовнішнього ключа)
-- Створення нової таблиці з category_id та зовнішніми ключами
CREATE TABLE expenses_new (
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
);

-- Копіювання даних зі старої таблиці (category_id буде NULL)
INSERT INTO expenses_new (id, expense_name, amount, user_id)
SELECT id, expense_name, amount, user_id FROM expenses;

-- Видалення старої таблиці
DROP TABLE expenses;

-- Перейменування нової таблиці
ALTER TABLE expenses_new RENAME TO expenses;