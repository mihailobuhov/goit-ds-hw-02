import sqlite3
from random import choice, randint

from faker import Faker



NUMBER_USERS = 10
STATUS = [('new',), ('in progress',), ('completed',)]
NUMBER_TASKS = 20
fake_data = Faker()
def generate_fake_data(number_users, number_tasks)->tuple:
    fake_users = [(fake_data.name(), fake_data.email()) for _ in range(number_users)]

    fake_tasks = []
    fake_description = []

    for _ in range(number_tasks):
        fake_tasks.append(fake_data.sentence())

    for _ in range (number_tasks):
        fake_description.append(fake_data.paragraph(nb_sentences=2))
        

    return fake_users, fake_tasks, fake_description

def prepare_data(users,tasks,descriptions)->tuple:
    for_users =[]
    for name,email in users:
        for_users.append((name,email), )



    for_status = STATUS

    for_tasks = []
    for task in tasks:
        for_tasks.append((task, choice(descriptions), randint(1, 3), randint(1,NUMBER_USERS) ))
    return for_users,for_tasks,for_status

def insert_data_to_db(users,tasks,status):

    with sqlite3.connect('tasks.db') as con:

        cur = con.cursor()
        sql_to_users = '''INSERT INTO users(fullname,email) VALUES (?, ?) '''

        cur.executemany(sql_to_users,users)


        sql_to_status = '''INSERT OR IGNORE INTO status(name) VALUES (?) '''
        cur.executemany(sql_to_status,status)

        sql_to_tasks = '''INSERT INTO tasks(title, description,status_id,user_id) VALUES (?,?,?,?) '''
        cur.executemany(sql_to_tasks,tasks)

        con.commit()


if __name__ == "__main__":
    users,tasks,status = prepare_data(*generate_fake_data(NUMBER_USERS,NUMBER_TASKS))
    insert_data_to_db(users, tasks, status)



