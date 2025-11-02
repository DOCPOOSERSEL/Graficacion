import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)

while(True):
    ret, img = cap.read()
    if ret:
        cv.imshow('video', img)
        img2 = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        cv.imshow('video1',img2)
        x,y=img2.shape
        for i in range(x):
            for j in range(y):
                if(img2[i,j]>150):
                        img2[i,j]=255
                else:
                        img2[i,j]=0

        cv.imshow('negativo', img2)
        k =cv.waitKey(1) & 0xFF
        if k == 27 :
            break
    else:
        break
   
cap.release()
cv.destroyAllWindows()