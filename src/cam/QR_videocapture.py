import cv2
import time

def scanQR():

    camera_id = 0
    delay = 1
    start_time = time.time()
    window_name = 'ReagentFlow QR scan'

    qcd = cv2.QRCodeDetector()
    cap = cv2.VideoCapture(0)

    while True:
        codeExit = False
        result = "NONE"

        ret, frame = cap.read()

        if ret:
            ret_qr, decoded_info, points, _ = qcd.detectAndDecodeMulti(frame)
            if ret_qr:
                for s, p in zip(decoded_info, points):
                    if s and s[0] == "R" and s[4] == "F" and s[5] == "0" and s[6] == "x":
                        result = s
                        codeExit = True
                    else:
                        color = (0, 0, 255)
                    frame = cv2.polylines(frame, [p.astype(int)], True, color, 8)
            frame = cv2.resize(frame, None, fx=0.5, fy=0.5)
            cv2.imshow(window_name, frame)
            if codeExit == True:
                break

        if time.time() - start_time > 20:
            print("Function has been running for more than 20 seconds without a result.")
            break

        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break

    cv2.destroyWindow(window_name)
    return result
