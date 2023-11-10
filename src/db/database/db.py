import sqlite3
from sqlite3 import Error

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def execute_get(connection, query): 
    cursor = connection.cursor()
    res = 0
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
    res = cursor.fetchone()
    if res is None:
        raise Exception("This item doesn't exist")
    return list(res)

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def execute_query_update(connection, query, mass, id):
    cursor = connection.cursor()
    try:
        cursor.execute(query, (mass,id))
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

if __name__ == '__main__':
    pass
