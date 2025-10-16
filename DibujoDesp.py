import cv2 as cv
import numpy as np

img = np.ones((500,500,3),np.uint8)*150
cv.circle(img,(30,30), 20 ,(23,43,144), -1)
cv.rectangle(img,(10,10), (200,200), (34,56,100), -1 )
cv.line(img,(255,255), (200,100),(23,244,144), 4)
for i in range(400):
    img= np.ones( (200,500,3),np.uint8)*150
    cv.circle(img, (i,i), 6, (255,0,0), -1)
    cv.imshow('img',img)
    # si no ponemos el imshow solo deja el rastro
    cv.waitKey(30)

#puntex es una funcion para poner texto y cambiar los valores del textos
#cv.poline para hacer figuras 

cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()