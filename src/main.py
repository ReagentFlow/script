from db import db_main
from cam import QR_videocapture
import cv2
from db.database import db
import numpy as np
from scales.scales_main import getting_weight

if __name__ == "__main__":
    key = QR_videocapture.scanQR()
    print(key)
    connection = db.create_connection('./db/database/ReagentFlowDB.db')
    weight = getting_weight()
    db_main.update(connection, key, weight)
    connection.close()