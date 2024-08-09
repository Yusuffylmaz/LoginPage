import sqlite3 as sql

def create_table():
    conn = sql.connect("kaydol.db")
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS kaydol("
                   "isim text,"
                   "soyisim text,"
                   "eposta text,"
                   "sifre text)")
    conn.commit()
    conn.close()
create_table()

def insert(isim,soyisim,eposta,sifre):
    conn = sql.connect("kaydol.db")
    cursor = conn.cursor()

    execute_add = "INSERT INTO kaydol VALUES {}"
    data= (isim,soyisim,eposta,sifre)
    cursor.execute(execute_add.format(data))

    conn.commit()
    conn.close()