from black import out
import cv2
import numpy as np


video=cv2.VideoCapture('fire_video.mov')

while True:
    ret, frame = video.read()
    frame =cv2.resize(frame, (1000, 600))
    blur =cv2.GaussianBlur(frame, (15,15), 0)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

    lower = [18,50,50]
    upper = [35,255,255]

    lower = np.array(lower, dtype='uint8')
    upper = np.array(upper, dtype='uint8')

    mask = cv2.inRange(hsv,lower,upper)

    output=cv2.bitwise_and(frame,hsv,mask=mask)
    
    number_of_total = cv2.countNonZero(mask)

    if int(number_of_total) > 15000:
        print('fire detected')


    if ret == False:
        break
    cv2. imshow("Output", output)

    if cv2. waitKey(1)& 0xFF == ord("q"):
        break
cv2. destroyAllWindows ()
video.release()