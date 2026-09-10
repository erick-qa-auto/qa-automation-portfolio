import sqlite3
import os

def test_carel_parts_count():
    DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "warehouse.db")
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT name, price FROM parts WHERE brand = 'Carel'")
    result = cur.fetchall()
    assert len(result) == 2
    conn.close()
