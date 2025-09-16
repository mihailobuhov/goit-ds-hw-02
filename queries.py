import sqlite3

def run_query(query, params=None):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results

def get_tasks_by_user(user_id):
    return run_query("SELECT * FROM tasks WHERE user_id = ?", (user_id,))
