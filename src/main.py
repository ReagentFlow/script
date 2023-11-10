from db import db_main
from cam import QR_videocapture
import cv2
from db.database import db
import numpy as np

key = QR_videocapture.scanQR()
connection = db.create_connection('./db/database/ReagentFlowDB.db')
db_main.update(connection, key, np.random.randint(1,200))
connection.close()
