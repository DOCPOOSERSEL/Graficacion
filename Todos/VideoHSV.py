import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)

while(True):
    ret, img = cap.read()
    if ret:
        cv.imshow('video', img)
        hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        cv.imshow('video1',hsv)
        uba=(90, 255, 255)
        ubb=(40, 40 ,40)
        uba2=(80, 255, 255)
        ubb2=(30, 30,30)
        mask1 = cv.inRange(hsv, ubb, uba)
        mask2 = cv.inRange(hsv, ubb2, uba2)
        mask = mask1+mask2
        res = cv.bitwise_and(img, img, mask=mask)
        cv.imshow('FiltroVerde', res)
        k =cv.waitKey(1) & 0xFF
        if k == 27 :
            break
    else:
        break
   
cap.release()
cv.destroyAllWindows()