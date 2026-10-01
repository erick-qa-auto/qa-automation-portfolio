import sqlite3
import os
...
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "multitable.db")
conn = sqlite3.connect(DB_PATH)

cur = conn.cursor()

cur.execute("PRAGMA table_info('parts')")
print(cur.fetchall())