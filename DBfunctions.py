import sqlite3
from sqlite3 import Error


def sql_connection():
    try:
        con = sqlite3.connect('myBase.db')
        return con
    except Error:
        print(Error)


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

#'id': 518356070, 'is_bot': False, 'first_name': 'OLEKSANDR', 'username': None, 'last_name': 'BEDINOV', 'language_code': 'ru'
