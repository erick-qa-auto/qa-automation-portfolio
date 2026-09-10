
import sqlite3
import os
...
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "warehouse.db")
conn = sqlite3.connect(DB_PATH)

cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS parts")
cur.execute("""
    CREATE TABLE parts (
        id INTEGER PRIMARY KEY,
        name TEXT,
        brand TEXT,
        price REAL,
        stock INTEGER
    )
""")

parts = [
    (1, "Контроллер E5-3200", "Carel", 18500, 4),
    (2, "Датчик температуры NTC", "Carel", 1200, 25),
    (3, "Компрессор MLZ066", "Danfoss", 42000, 2),
    (4, "Реле давления KP5", "Danfoss", 6800, 7),
    (5, "ТЭН 3 кВт", "Unox", 5400, 3),
    (6, "Вентилятор обдува", "Eliwell", 3900, 0),
]
cur.executemany("INSERT INTO parts VALUES (?, ?, ?, ?, ?)", parts)
conn.commit()

for row in cur.execute("SELECT * FROM parts"):
    print(row)

for row in cur.execute("SELECT name, price FROM parts WHERE brand = 'Carel'"):
    print(row)

print(len(parts))

conn.close()