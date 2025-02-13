import cv2

cam=cv2.VideoCapture(0)

while True:
    ignore, frame = cam.read()
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('my WEBcam', grayFrame)
    cv2.moveWindow('my WEBcam', 0, 0)

    if cv2.waitKey(1) == ord('q'):
        break
cam.release()