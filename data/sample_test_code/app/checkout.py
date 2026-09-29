import sqlite3

API_KEY = "sk_live_99887766554433221100"

def get_user_data(user_input):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    # SQL injection vulnerability
    query = f"SELECT * FROM users WHERE username = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()
