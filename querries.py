import sqlite3

#Отримати всі завдання певного користувача.

def get_user_tasks()->list:
    sql = '''SELECT u.fullname, t.title, t.description 
FROM tasks AS t
JOIN users AS u
ON t.user_id = u.id 
WHERE t.user_id = 6
'''
    with sqlite3.connect('tasks.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


#Вибрати завдання за певним статусом. Використайте підзапит для вибору завдань з конкретним статусом, наприклад, 'new'.

def get_task_by_status()->list:
    sql = '''SELECT  t.title, t.description
FROM tasks AS t
WHERE t.status_id = (
	SELECT id FROM status
	WHERE name = 'new'
	);
    '''
    with sqlite3.connect('tasks.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


#Оновити статус конкретного завдання. Змініть статус конкретного завдання на 'in progress' або інший статус.

def update_task_status()->list:
    sql = '''
    UPDATE tasks
SET status_id = (SELECT id FROM status WHERE name = 'in progress')
WHERE id = 5;
    '''
    with sqlite3.connect ('tasks.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

#Отримати список користувачів, які не мають жодного завдання. Використайте комбінацію SELECT, WHERE NOT IN і підзапит.

def get_users_without_tasks()->list:
    sql = '''
    SELECT u.fullname
FROM users AS u
WHERE u.id NOT IN (SELECT user_id FROM tasks);
    '''
    with sqlite3.connect('tasks.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


# Додати нове завдання для конкретного користувача. Використайте INSERT для додавання нового завдання.

def add_new_task()->list:
    sql = '''
    INSERT INTO tasks (title,description,status_id,user_id)
VALUES(
'do homework',
'english',
(SELECT id FROM status WHERE name = 'new' ),
(SELECT id FROM users WHERE fullname = 'Beth King')
);
    '''

    with sqlite3.connect('tasks.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


#Отримати всі завдання, які ще не завершено. Виберіть завдання, чий статус не є 'завершено'

def get_uncompleted_tasks()->list:
    sql = '''
    SELECT title,description,status_id
FROM tasks
WHERE status_id IN (SELECT id FROM status WHERE name !='completed' );
    '''
    with sqlite3.connect('tasks.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

#Знайти користувачів з певною електронною поштою.
# Використайте SELECT із умовою LIKE для фільтрації за електронною поштою.

def get_users_by_email():
    sql = '''SELECT fullname,email
FROM  users
WHERE email LIKE '%@example.org';'''
    with sqlite3.connect('tasks.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

#Оновити ім'я користувача. Змініть ім'я користувача за допомогою UPDATE

def update_user_name()->list:
    sql = '''
UPDATE users
SET fullname = 'Sara Jakson'
WHERE id = 8;
'''

    with sqlite3.connect('tasks.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

'''Отримати кількість завдань для кожного статусу. 
Використайте SELECT, COUNT, GROUP BY для групування завдань за статусами.
'''

def count_tasks_by_status()-> list:
    sql = '''
    SELECT s.name AS status,COUNT (t.title) AS quantity
FROM tasks AS t
LEFT JOIN status AS s
ON t.status_id = s.id 
GROUP BY s.name;
    '''
    with sqlite3.connect('tasks.db') as con:
        cur = con.cursor()
        cur.execute(sql)
    return cur.fetchall()


'''
Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти.
 Використайте SELECT з умовою LIKE в поєднанні з JOIN, щоб вибрати завдання,
  призначені користувачам, чия електронна пошта містить певний домен (наприклад, '%@example.com').
'''

def get_task_by_email()->list:
    sql = '''
    SELECT t.title, t.description, u.email
FROM tasks AS t
JOIN users AS u
ON t.user_id = u.id 
WHERE u.email LIKE '%@example.com';
    '''
    with sqlite3.connect('tasks.db') as con:
        cur = con.cursor()
        cur.execute(sql)
    return cur.fetchall()

'''
Отримати список завдань, що не мають опису. Виберіть завдання, у яких відсутній опис.
'''

def get_title_without_description()->list:
    sql = '''
    SELECT title
FROM tasks
WHERE description IS NULL 
OR description = '';
    '''

    with sqlite3.connect('tasks.db') as con:
        cur = con.cursor()
        cur.execute(sql)
    return cur.fetchall()


'''
Вибрати користувачів та їхні завдання, які є у статусі 'in progress'. 
Використайте INNER JOIN для отримання списку користувачів та їхніх завдань із певним статусом.
'''

def get_users_by_status()->list:
    sql = '''
    SELECT u.fullname, t.title,t.description,s.name
FROM users AS u
JOIN tasks AS t
ON t.user_id = u.id  
JOIN status AS s
ON t.status_id = s.id 
WHERE s.name = 'in progress';
    '''

    with sqlite3.connect('tasks.db') as con:
        cur = con.cursor()
        cur.execute(sql)
    return cur.fetchall()

'''
Отримати користувачів та кількість їхніх завдань.
Використайте LEFT JOIN та GROUP BY для вибору користувачів та підрахунку їхніх завдань.
'''

def count_task_by_user()->list:
    sql = '''
    SELECT u.fullname, COUNT(t.title) AS task_count
FROM users AS u
LEFT JOIN tasks AS t
ON u.id = t.user_id 
GROUP BY  u.fullname  ;
    '''
    with sqlite3.connect('tasks.db') as con:
        cur = con.cursor()
        cur.execute(sql)
    return cur.fetchall()
