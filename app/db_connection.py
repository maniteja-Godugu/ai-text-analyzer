import sqlite3

def get_connection():
    conn = sqlite3.connect("analyze.db")
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    conn=get_connection()
    cursor=conn.cursor()
    create_table_query="""CREATE TABLE IF NOT EXISTS analyze
    (
    SI_NO INTEGER PRIMARY KEY AUTOINCREMENT,
    Prompt TEXT NOT NULL,
    Summary TEXT NOT NULL,
    Sentimenti TEXT NOT NULL,
    Difficulty TEXT NOT NULL

    )"""
    cursor.execute(create_table_query)
    conn.commit()
    conn.close()
    

create_table()
