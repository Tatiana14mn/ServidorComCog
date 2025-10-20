import sqlite3
def init_db():
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS productos (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nombre TEXT NOT NULL,categoria TEXT,cantidad INTEGER,precio REAL)""")
    conn.commit()
    conn.close()