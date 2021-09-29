import sqlite3

conn = sqlite3.connect('C:\\Users\\admin\\AppData\\Roaming\\JetBrains\\DataGrip2020.3\\projects\\u3m2challenge\\demo_data.sqlite3')
c = conn.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS demo (s TEXT, x REAL, y REAL)')


def data_entry():
    c.execute("INSERT INTO demo(s, x, y) VALUES('g',3,9),('v',5,7),('f',8,7)")
    conn.commit()
#    c.close()
#    conn.close()


def clear_table():
    c.execute("DELETE FROM demo")
    conn.commit()
    c.close()
    conn.close


#create_table()
#data_entry()
#clear_table()


def count_table():
    c.execute("SELECT COUNT(*) FROM demo")
    c_result = c.fetchone()
    print(c_result)
#    c.close()
#    conn.close

def select_count():
    c.execute("SELECT COUNT(*) FROM demo WHERE x >= 5 AND y >= 5")
    c_result = c.fetchone()
    print(c_result)

def unique_y():
    c.execute("SELECT COUNT(DISTINCT y) FROM demo")
    c_result = c.fetchone()
    print(c_result)

count_table()
select_count()
unique_y()
