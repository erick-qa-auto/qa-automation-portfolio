import sqlite3
import os
import logging

# Настраиваем логгер: показываем время, уровень (INFO) и само сообщение
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def test_carel_parts():
    DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "warehouse.db")
    conn = sqlite3.connect(DB_PATH)   # 1. для поиска пути к БД и подключения
    cur = conn.cursor()               # 2. для создания курсора
    cur.execute("SELECT name, price FROM parts WHERE brand = 'Carel'")
    result = cur.fetchall()          # 4. Забираем всё в переменную rows через fetchall()
    assert len(result)>0
    logging.info("✔[DB] Successfully fetched records")
    assert result[0][0] == "Контроллер E5-3200"
    logging.info("✔[Assert] Part name validated")
    assert result[0][1] == 18500
    logging.info("✔[Assert] Part price validated")
    conn.close()