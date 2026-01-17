import sqlite3

def run_user_code(user_input):
    # ❌ CRITICAL: Code Injection (eval)
    return eval(user_input)

def get_user(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # ❌ CRITICAL: SQL Injection
    query = f"SELECT * FROM users WHERE id = '{user_id}'"
    cursor.execute(query)

    return cursor.fetchall()
