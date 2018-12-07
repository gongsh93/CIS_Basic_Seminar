import sqlite3 #python의 기본 내장 DB 프로그램

def create_DB():
    conn = sqlite3.connect("my.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE notices (idx integer primary key autoincrement, title text, date date);")
    conn.commit()

def show_DB():
    conn = sqlite3.connect("my.db")
    cur = conn.cursor()
    cur.execute("SELECT idx, title, date FROM notices;")
    # SELECT * FROM notices WHERE title="인재개발원~~" AND DATE > '2018-11-01' ORDER BY idx DESC;
    results = cur.fetchall()
    for result in results:
        print(result)

def insert_DB(notices):
    conn = sqlite3.connect("my.db")
    cur = conn.cursor()
    for notice in notices:
        cur.execute("INSERT INTO notices(title, date) VALUES('%s', '%s');" % (notice[0], notice[1]))
    conn.commit() # commit을 안하면 저장이 안됨

def delete_DB():
    conn = sqlite3.connect("my.db")
    cur = conn.cursor()
    cur.execute("DELETE * FROM notices;")
    conn.commit()