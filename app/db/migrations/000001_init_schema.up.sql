-- UP: Створення ініціюючої схеми бази даних (users, categories, expenses)

-- 1. Таблиця Користувачів (users)
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    user_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL
);

-- 2. Таблиця Категорій (categories)
CREATE TABLE categories (
    id INTEGER PRIMARY KEY,
    category TEXT NOT NULL UNIQUE
);

-- 3. Заповнення таблиці categories початковими даними
INSERT INTO categories (category) VALUES
    ('Home'),
    ('Entertainment'),
    ('Transport'),
    ('Food'),
    ('Health');

-- 4. Таблиця Витрат (expenses)
-- amount зберігається як INTEGER (у копійках/центах) для точності
CREATE TABLE expenses (
    id INTEGER PRIMARY KEY,
    expense_name TEXT NOT NULL,
    amount INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    category_id INTEGER,
    
    -- Зовнішній ключ: Зв'язок з користувачем
    CONSTRAINT fk_user_id
    FOREIGN KEY (user_id)
    REFERENCES users(id) ON DELETE CASCADE,
    
    -- Зовнішній ключ: Зв'язок з категорією
    -- Використовуємо ON DELETE SET NULL, щоб витрата не видалялася, якщо категорія зникає
    CONSTRAINT fk_categ_id
    FOREIGN KEY (category_id)
    REFERENCES categories(id) ON DELETE SET NULL
);