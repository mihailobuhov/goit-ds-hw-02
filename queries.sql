-- Отримати всі завдання певного користувача
SELECT * FROM tasks WHERE user_id = 1;

-- Отримати користувачів без завдань
SELECT * FROM users WHERE id NOT IN (SELECT user_id FROM tasks);
