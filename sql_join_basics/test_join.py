import sqlite3
import os
...
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "multitable.db")
conn = sqlite3.connect(DB_PATH)

cur = conn.cursor()

cur.execute("SELECT p.name, s.company_name FROM parts AS p INNER JOIN suppliers AS s ON p.supplier_id = s.id")
print(cur.fetchall())
