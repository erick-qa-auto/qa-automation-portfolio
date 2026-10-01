import sqlite3
import os
...
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "multitable.db")
conn = sqlite3.connect(DB_PATH)

cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS parts (
        id INTEGER PRIMARY KEY,
        name TEXT,
        brand TEXT,
        price REAL,
        stock INTEGER,
        supplier_id INTEGER
    )
""")

parts_data = [
    (1, "Контроллер E5-3200", "Carel", 18500, 4, 1),
    (2, "Датчик температуры NTC", "Carel", 1200, 25, 1),
    (3, "Компрессор MLZ066", "Danfoss", 42000, 2, 2),
    (4, "Реле давления KP5", "Danfoss", 6800, 7, 2),
    (5, "ТЭН 3 кВт", "Unox", 5400, 3, 3),
    (6, "таймер 90 мин", "Unox", 4500, 7, 3),
    (7, "Вентилятор обдува", "Eliwell", 3900, 0, 4),
    (8, "Контроллер ID974", "Eliwell", 5000, 2, 4),
]
cur.executemany("INSERT INTO parts VALUES (?, ?, ?, ?, ?, ?)", parts_data)

cur.execute("""
    CREATE TABLE IF NOT EXISTS suppliers (
        id INTEGER PRIMARY KEY,
        company_name TEXT,
        country TEXT
    )
""")

suppliers_data = [
    (1, "Carel", "Italy"),
    (2, "Danfoss", "Denmark"),
    (3, "Unox", "Italy"),
    (4, "Eliwell", "Slovenia")
]
cur.executemany("INSERT INTO suppliers VALUES (?, ?, ?)", suppliers_data)
conn.commit()
conn.close()