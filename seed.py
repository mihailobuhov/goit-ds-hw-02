import sqlite3
from faker import Faker
import random

def seed_database():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    fake = Faker()

    statuses = ['new', 'in progress', 'completed']
    cursor.executemany("INSERT OR IGNORE INTO status (name) VALUES (?)", [(s,) for s in statuses])

    users = [(fake.name(), fake.unique.email()) for _ in range(10)]
    cursor.executemany("INSERT INTO users (fullname, email) VALUES (?, ?)", users)

    cursor.execute("SELECT id FROM users")
    user_ids = [row[0] for row in cursor.fetchall()]
    cursor.execute("SELECT id FROM status")
    status_ids = [row[0] for row in cursor.fetchall()]

    tasks = [
        (
            fake.sentence(nb_words=4),
            fake.text(max_nb_chars=200) if random.choice([True, False]) else None,
            random.choice(status_ids),
            random.choice(user_ids)
        )
        for _ in range(30)
    ]
    cursor.executemany("INSERT INTO tasks (title, description, status_id, user_id) VALUES (?, ?, ?, ?)", tasks)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    seed_database()
