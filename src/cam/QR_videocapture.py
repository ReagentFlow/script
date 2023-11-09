import cv2
import time

def scanQR():
    camera_id = 0
    frame_display_delay = 1
    window_name = 'ReagentFlow QR scan'
    start_time = time.time()  # Get the current time

    qr_detector = cv2.QRCodeDetector()
    video_capture = cv2.VideoCapture(camera_id)

    while True:
        code_detected = False
        qr_result = "NONE"

        ret, frame = video_capture.read()

        if ret:
            ret_qr, decoded_info, points, _ = qr_detector.detectAndDecodeMulti(frame)
            if ret_qr:
                for decoded_text, qr_points in zip(decoded_info, points):
                    if decoded_text and decoded_text[0] == "R" and decoded_text[4] == "F" and decoded_text[5] == "0" and decoded_text[6] == "x":
                        qr_result = decoded_text
                        code_detected = True
                        color = (0, 255, 0)
                    else:
                        color = (0, 0, 255)
                    frame = cv2.polylines(frame, [qr_points.astype(int)], True, color, 8)
            frame = cv2.resize(frame, None, fx=0.5, fy=0.5)
            cv2.imshow(window_name, frame)
            if code_detected:
                break

        if time.time() - start_time > 20:
            print("Function has been running for more than 20 seconds without a result.")
            break

        if cv2.waitKey(frame_display_delay) & 0xFF == ord('q'):
            break

    cv2.destroyWindow(window_name)
    return qr_result
