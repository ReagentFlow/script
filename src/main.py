from db import db_main
from cam import QR_videocapture
import cv2
from db.database import db

key = QR_videocapture.scanQR()
connection = db.create_connection('./db/database/ReagentFlowDB.db')
db_main.update(connection, key, 1000)
connection.close()
