-- DOWN: Видаляє таблицю categories та видаляє стовпець category_id з expenses

-- 1. Оновлення таблиці expenses (перебудова для видалення стовпця category_id)
-- Створення тимчасової таблиці БЕЗ category_id
CREATE TABLE expenses_old (
    id INTEGER PRIMARY KEY,
    expense_name TEXT NOT NULL,
    amount REAL NOT NULL,
    user_id INTEGER,
    CONSTRAINT fk_user_id
    FOREIGN KEY (user_id)
    REFERENCES users(id) ON DELETE CASCADE
);

-- Копіювання даних (category_id ігнорується)
INSERT INTO expenses_old (id, expense_name, amount, user_id)
SELECT id, expense_name, amount, user_id FROM expenses;

-- Видалення поточної таблиці
DROP TABLE expenses;

-- Перейменування старої таблиці
ALTER TABLE expenses_old RENAME TO expenses;

-- 2. Видалення таблиці categories
DROP TABLE categories;