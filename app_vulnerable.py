import sqlite3

# ❌ Hardcoded credentials (Security Hotspot)
DB_PASSWORD = "admin123"

def get_user_data(user_id):
    # ❌ SQL Injection vulnerability
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    query = f"SELECT * FROM users WHERE id = '{user_id}'"
    cursor.execute(query)

    data = cursor.fetchall()
    connection.close()
    return data

def run_user_code(user_input):
    # ❌ Use of eval (Critical Security Issue)
    return eval(user_input)

def read_file(file_path):
    try:
        file = open(file_path, "r")
        return file.read()
    except:
        # ❌ Broad exception catch (Code Smell)
        return "Error occurred"

if __name__ == "__main__":
    print(get_user_data("1 OR 1=1"))
    print(run_user_code("__import__('os').system('ls')"))
