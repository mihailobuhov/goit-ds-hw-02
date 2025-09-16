import sqlite3
import os

def initialize_database():
    if not os.path.exists("tasks.db"):
        print("Creating database and tables...")
        conn = sqlite3.connect("tasks.db")
        with open("create_tables.sql", "r") as f:
            conn.executescript(f.read())
        conn.close()
        print("Done.")
    else:
        print("Database already exists.")

if __name__ == "__main__":
    initialize_database()

    from seed import seed_database
    from queries import get_tasks_by_user

    seed_database()
    print("Database seeded.")

    tasks = get_tasks_by_user(1)
    for task in tasks:
        print(task)
