-- DOWN: Видаляє стовпець category_id з expenses та видаляє таблицю categories

-- 1. Видалення стовпця category_id (Використовуємо нову команду DROP COLUMN)
-- Увага: Ця команда працює лише у SQLite версії 3.35.0 або новішій.
ALTER TABLE expenses DROP COLUMN category_id;

-- 2. Видалення таблиці categories
DROP TABLE categories;