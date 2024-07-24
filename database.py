import sqlite3

def init_db():
    conn = sqlite3.connect('logs.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id TEXT PRIMARY KEY,
            domain TEXT,
            upload_date TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_log(log_id, domain, upload_date):
    conn = sqlite3.connect('logs.db')
    c = conn.cursor()
    c.execute('INSERT INTO logs (id, domain, upload_date) VALUES (?, ?, ?)', (log_id, domain, upload_date))
    conn.commit()
    conn.close()

def get_logs():
    conn = sqlite3.connect('logs.db')
    c = conn.cursor()
    c.execute('SELECT * FROM logs')
    logs = c.fetchall()
    conn.close()
    return logs
