import sqlite3
import os

def test_danfoss_prices():
    DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "warehouse.db")
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT name, price FROM parts WHERE brand = 'Danfoss'")
    rows = cur.fetchall()
    print(rows)
    assert len(rows) > 0 # проверили что не пусто
    print("successfull records")
    assert len(rows) == 2 # проверили длину
    print("The len is correct.")
    conn.close()