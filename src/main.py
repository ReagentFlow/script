from db import db_main
from scanner.scanner import barcode_scanner
from db.database import db
import numpy as np
from scales.scales_main import getting_weight

if __name__ == "__main__":
    key = barcode_scanner()
    print(key)
    if key != "NONE":
        weight = getting_weight()
        # print(weight)
        connection = db.create_connection('/Volumes/MacintoshHD/test2/script/src/db/database/ReagentFlowDB.db')
        # print(type(connection))
        db_main.update(connection, key, weight)
        connection.close()
    else:
        print('error with scanning')
