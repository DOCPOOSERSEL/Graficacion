import cv2 as cv
import numpy as np

img = np.ones((500,500,3),np.uint8)*150
cv.rectangle(img, (150, 250), (350, 450), (180, 100, 70), -1)   # paredes

# Puerta
cv.rectangle(img, (230, 350), (270, 450), (100, 60, 30), -1)    # puerta

# Ventana
cv.rectangle(img, (170, 280), (210, 320), (255, 255, 255), -1)  # Ventana blanca
cv.rectangle(img, (170, 280), (210, 320), (0, 0, 0), 2)         # Borde negro

# Techo
pts = np.array([[150, 250], [350, 250], [250, 150]], np.int32)  # puntos del triángulo
cv.fillPoly(img, [pts], (150, 50, 50)) # Relleno del triangulo

cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()