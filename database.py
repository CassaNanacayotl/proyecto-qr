import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect('qr_system.db')
    c = conn.cursor()
    
    # Tabla para los QR generados
    c.execute('''
        CREATE TABLE IF NOT EXISTS qr_codes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticket_id TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            created_at TIMESTAMP NOT NULL,
            used BOOLEAN DEFAULT FALSE,
            used_at TIMESTAMP,
            verification_code TEXT NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()

def get_db():
    conn = sqlite3.connect('qr_system.db')
    conn.row_factory = sqlite3.Row
    return conn