import cv2
from screeninfo import get_monitors

# camera & screen setup
cap = cv2.VideoCapture(0)
screen = get_monitors() .pop()
cap.set(3, screen.width)
cap.set(4, screen.height)


while True:
    success, img = cap.read()
    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
