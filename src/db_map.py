import sqlite3


with sqlite3.connect('My_DB.db') as con:
    sql = con.cursor()
            
    # sql.execute("DROP TABLE IF EXISTS Media_ids")
    # sql.execute(
        # """
            # CREATE TABLE IF NOT EXISTS Media_ids (
                # id INTEGER PRIMARY KEY AUTOINCREMENT,
                # file_id TEXT(255),
                # filename TEXT(255)
            # )
        # """
    # )
    
sql.execute("SELECT * FROM Media_ids")
records = sql.fetchall()
print(records)
for record in records:
    print(record)