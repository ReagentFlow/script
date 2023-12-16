import sys
import sqlite3
from db.database import db
#from database.db import execute_query, execute_query_update, execute_get

def data_from_qr(data):
    pos_end_of_num_container = 0
    for i, character in enumerate(data):
        if 'F' == character:
            pos_end_of_num_container = i
    num_of_container = data[1:pos_end_of_num_container]
    cas = data[pos_end_of_num_container+3:]
    return [int(num_of_container), cas]

def update(connection, str, mass: int):
    id_container, cas = data_from_qr(str)

    # does it exsist?
    req_except = f"""SELECT * from tab WHERE id = {id_container}"""
    t = db.execute_get(connection, req_except)
    if t is None:
        raise Exception("This item doesn't exist")

    # getting mass of container
    req = f"""SELECT mass_cont from (SELECT * from tab WHERE id = {id_container})"""
    mass_cont = db.execute_get(connection, req)[0]
    # begin updating
    updater = """
    UPDATE
      tab
    SET
      mass = ?
    WHERE
      id = ?
    """
    db.execute_query_update(connection, updater, (mass-mass_cont), id_container)

if __name__ == '__main__':
    pass
