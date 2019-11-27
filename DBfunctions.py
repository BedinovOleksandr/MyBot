import sqlite3
from sqlite3 import Error


def sql_connection():
    try:
        con = sqlite3.connect('myBase.db')
        return con
    except Error:
        print(Error)

sql_connection().cursor().execute("""create table if not exists user
(
	id INTEGER,
	is_bot INTEGER,
	first_name TEXT,
	username TEXT,
	last_name TEXT,
	language_code TEXT
);
""")


# Using user id
def сheck_user_if_exist(id):
    quary = f"""SELECT id FROM 'user' where id = {id} """
    print(quary)
    cursor = sql_connection().cursor()
    cursor.execute(quary)
    if cursor.fetchone() == None:
        return True
    else:
        return False


def insert_user(args):
    if сheck_user_if_exist(args[0]):
        quary = f"""INSERT INTO 'user' values ({args[0]},{args[1]},'{args[2]}','{args[3]}','{args[4]}','{args[5]}')"""
        print(quary)
        conn = sql_connection()
        cursor = conn.cursor()
        cursor.execute(quary)
        conn.commit()
        cursor.close()
    else:
        pass


sql_connection().close()
