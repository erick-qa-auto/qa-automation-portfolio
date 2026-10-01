import pytest
import sqlite3
import os

@pytest.fixture(autouse=True)
def db_cur():
    # 1. Путь к базе и подключение
    DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "multitable.db")
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # 2. Создание таблиц (строим полки)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS suppliers (
            id INTEGER PRIMARY KEY,
            company_name TEXT,
            country TEXT
        )
    """)
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

    # 3. Заполнение данными (раскладываем товары)
    suppliers_data = [
        (1, "Carel", "Italy"),
        (2, "Danfoss", "Denmark"),
        (3, "Unox", "Italy"),
        (4, "Eliwell", "Slovenia")
    ]
    cur.executemany("INSERT OR IGNORE INTO suppliers VALUES (?, ?, ?)", suppliers_data)

    parts_data = [
        (1, "Контроллер E5-3200", "Carel", 15000, 10, 1),
        (2, "Датчик температуры NTC", "Carel", 2500, 50, 1),
        (3, "Компрессор MLZ066", "Danfoss", 45000, 5, 2),
        (4, "Реле давления KP5", "Danfoss", 3500, 20, 2),
        (5, "ТЭН 3 кВт", "Unox", 8000, 15, 3),
        (6, "таймер 90 мин", "Unox", 1200, 30, 3),
        (7, "Вентилятор обдува", "Eliwell", 4000, 25, 4),
        (8, "Контроллер ID974", "Eliwell", 18000, 8, 4)
    ]
    cur.executemany("INSERT OR IGNORE INTO parts VALUES (?, ?, ?, ?, ?, ?)", parts_data)
    
    conn.commit() # Сохраняем изменения в базе

    # 4. Передаем управление тесту
    yield cur

    # 5. Уборка после теста
    conn.close()
    os.remove(DB_PATH)