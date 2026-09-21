import sqlite3
import os

def test_fetch_methods():
    DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "warehouse.db")
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT name, price FROM parts ORDER BY price")
    row = cur.fetchone()
    print(row)
    print(row[0])
    print(row[1])
    cur.execute("SELECT name, price FROM parts ORDER BY price")
    rows = cur.fetchall()
    print(rows)
    print(rows[0][1])
    assert len(rows) == 6
    conn.close