import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while(True):
    #Captures frame by frame
    ret, frame = cap.read()
    #Operations on the frame comes here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #Displays the resulting frame
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()