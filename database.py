import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect('logs.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id TEXT PRIMARY KEY,
            domain TEXT,
            upload_date TEXT,
            upload_time TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_log(log_id, domain, upload_date, upload_time):
    conn = sqlite3.connect('logs.db')
    c = conn.cursor()
    c.execute('INSERT INTO logs (id, domain, upload_date, upload_time) VALUES (?, ?, ?, ?)', 
              (log_id, domain, upload_date, upload_time))
    conn.commit()
    conn.close()

def get_logs():
    conn = sqlite3.connect('logs.db')
    c = conn.cursor()
    c.execute('SELECT * FROM logs')
    logs = c.fetchall()
    conn.close()
    return logs
