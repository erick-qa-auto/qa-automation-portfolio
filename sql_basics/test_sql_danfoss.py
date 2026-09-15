import sqlite3
import os

def test_danfoss_parts():
    DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "warehouse.db")
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT name, price FROM parts WHERE brand = 'Danfoss'")
    result = cur.fetchall()                           #result = cur.fetchone()
    assert len(result) > 0                            #assert result is not None
    print("✅ [DB] Successfully fetched records")
    assert result[0][0] == "Компрессор MLZ066"        #assert result[0] == "Компрессор MLZ066"
    print("✅ [Assert] Part name validated") 
    assert result[0][1] == 42000                      #assert result[1] == 42000
    print("✅ [Assert] Part price validated")  
    conn.close()