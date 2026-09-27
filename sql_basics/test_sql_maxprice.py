import sqlite3
import os
import logging 

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def test_group_maxprice():
    DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "warehouse.db")
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT brand, MAX(price) FROM parts GROUP BY brand HAVING MAX(price) > 10000 ORDER BY MAX(price) DESC")
    result = cur.fetchall()
    logger.info(f"query result: {result}")
    assert len(result) > 0 , "проверили что не пусто"
    brand = result[0][0]
    assert result[0][0] == 'Danfoss', f"Expected brand 'Danfoss', got '{result[0][0]}'"
    logger.info(f"Part brand validate: {brand}")
    conn.close()
