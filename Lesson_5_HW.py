import cv2

cam=cv2.VideoCapture(0)

while True:
    ignore, frame = cam.read()
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    width = 640
    height = 480

    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam', 0, 0)

    cv2.imshow('my grayFrame', grayFrame)
    cv2.moveWindow('my grayFrame', width, 0)

    cv2.imshow('my WEBcam0', frame)
    cv2.moveWindow('my WEBcam0', width, height)

    cv2.imshow('my grayFrame0', grayFrame)
    cv2.moveWindow('my grayFrame0)', 0, height)

    if cv2.waitKey(1) == ord('q'):
        break
cam.release()