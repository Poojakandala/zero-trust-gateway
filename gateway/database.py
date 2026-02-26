import sqlite3
from datetime import datetime

DB_PATH = "audit.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS logs
                 (timestamp TEXT, client_ip TEXT, risk_score REAL, status TEXT)''')
    conn.commit()
    conn.close()

def log_transaction(ip, score, status):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO logs VALUES (?, ?, ?, ?)", 
              (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ip, score, status))
    conn.commit()
    conn.close()

# Initialize the DB when this script is imported
init_db()