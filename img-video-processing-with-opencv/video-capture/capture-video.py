import cv2, time

video=cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    check, frame = video.read()
    cv2.imshow("Window Capturing", frame)
    key=cv2.waitKey(1)

    if key==ord('q'):
        break

video.release()
cv2.destroyAllWindows()
