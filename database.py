import sqlite3
from datetime import datetime


DB_NAME = "todos.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS todos (
            sno INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            desc TEXT,
            date_created TEXT,
            status TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_todo(title, desc):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO todos (title, desc, date_created, status)
        VALUES (?, ?, ?, ?)
    """, (title, desc, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Pending"))
    conn.commit()
    conn.close()

def get_all_todos():
    conn = get_connection()
    cursor = conn.cursor()
    todos = cursor.execute("SELECT * FROM todos").fetchall()
    conn.close()
    return todos

def get_todo(sno):
    conn = get_connection()
    cursor = conn.cursor()
    todo = cursor.execute("SELECT * FROM todos WHERE sno = ?", (sno,)).fetchone()
    conn.close()
    return todo

def update_todo(sno, title, desc):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE todos SET title = ?, desc = ? WHERE sno = ?", (title, desc, sno))
    conn.commit()
    conn.close()

def delete_todo(sno):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM todos WHERE sno = ?", (sno,))
    conn.commit()
    conn.close()

def mark_completed(sno):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE todos SET status = ? WHERE sno = ?", ("Completed", sno))
    conn.commit()
    conn.close()