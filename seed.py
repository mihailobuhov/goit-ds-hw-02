from faker import Faker
import sqlite3
import random

fake = Faker()
conn = sqlite3.connect("task_manager.db")
cur = conn.cursor()

statuses = [('new',), ('in progress',), ('completed',)]
cur.executemany("INSERT INTO status (name) VALUES (?)", statuses)

for _ in range(5):
    cur.execute("INSERT INTO users (fullname, email) VALUES (?, ?)", (fake.name(), fake.email()))

user_ids = [row[0] for row in cur.execute("SELECT id FROM users").fetchall()]
status_ids = [row[0] for row in cur.execute("SELECT id FROM status").fetchall()]

for _ in range(10):
    cur.execute("""
        INSERT INTO tasks (title, description, status_id, user_id)
        VALUES (?, ?, ?, ?)""", (
        fake.sentence(nb_words=5),
        fake.text(),
        random.choice(status_ids),
        random.choice(user_ids)
    ))

conn.commit()
conn.close()
