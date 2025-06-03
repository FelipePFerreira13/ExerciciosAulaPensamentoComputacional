import sqlite3

def get_connection():
    conn = sqlite3.connect('my_database.db')
    return conn
