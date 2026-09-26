import sqlite3
import os
import logging 

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def test_group_methods():
    DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "warehouse.db")
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT brand, AVG(price) FROM parts GROUP BY brand HAVING AVG(price) > 5000 ORDER BY AVG(price) DESC")
    result = cur.fetchall()
    logger.info(f" query result:{result}")
    assert len(result) > 0, "Result is empty — but I'm not! Expected at least one brand with avg_price > 5000"
    assert result[0][1] > 5000, f"First brand avg_price {result[0][1]} should be > 5000"