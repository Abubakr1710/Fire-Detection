from black import out
import cv2
import numpy as np
import playsound


fire_reported = 0
alarm_status = False


def play_audio():
    playsound.playsound('alarm.mp3', True)


video=cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    blur =cv2.GaussianBlur(frame, (15,15), 0)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

    lower = [18,50,50]
    upper = [35,255,255]

    lower = np.array(lower, dtype='uint8')
    upper = np.array(upper, dtype='uint8')

    mask = cv2.inRange(hsv,lower,upper)

    output=cv2.bitwise_and(frame,hsv,mask=mask)
    
    size = cv2.countNonZero(mask)

    if int(size) > 1000:
        print('Fire detected')
        fire_reported = fire_reported + 1
        if fire_reported >= 1:
            if alarm_status == False:
                play_audio()
                alarm_status = True
    else:
        print('fire is not detecting')

    if ret == False:
        break
    cv2.imshow("Output", output)

    if cv2. waitKey(1)& 0xFF == ord("q"):
        break

cv2. destroyAllWindows ()
video.release()