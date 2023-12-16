from db import db_main
#from cam import QR_videocapture
from scanner.scanner import barcode_scanner
import cv2
from db.database import db
import numpy as np
from scales.scales_main import getting_weight

if __name__ == "__main__":
    key = barcode_scanner()
    print(key)
    if key != "NONE":
        connection = db.create_connection('./db/database/ReagentFlowDB.db')
        weight = getting_weight()
        db_main.update(connection, key, weight)
        connection.close()
    else:
        print('error with scanning')