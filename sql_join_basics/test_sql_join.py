import sqlite3
import os
import logging 

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)
...
def test_inner_join(db_cur):
    db_cur.execute("SELECT p.name, s.company_name FROM parts AS p INNER JOIN suppliers AS s ON p.supplier_id = s.id")
    result = db_cur.fetchall()
    logger.info(f" query result:{result}")
    assert len(result) > 0


def test_left_join_all_parts(db_cur):
    db_cur.execute("SELECT p.name, s.company_name FROM parts AS p LEFT JOIN suppliers AS s ON p.supplier_id = s.id")
    result = db_cur.fetchall()
    logger.info(f" query result:{result}")
    assert len(result) == 8, f"expected 8 lines, got {len(result)}"