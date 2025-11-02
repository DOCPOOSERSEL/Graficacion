import cv2 as cv
import numpy as np

# Cargar la imagen en escala de grises
img = cv.imread('TsuruRojo.jpg', 1)

# Definir el factor de escala
# Aplicar el escalado usando cv.resize()
img_escalada = cv.resize(img, None, fx=2, fy=2)
# Se crea la matriz del filtro de convolucion para tomar en cruz los pixeles para que se realce mejor la imagen
kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
# Se aplica el filtro y se usa el '-1' para que mantenga la misma profundidad que la imagen que fue escalada
filtrada = cv.filter2D(img_escalada,-1,kernel)

# Mostrar la imagen original y la escalada
cv.imshow('Imagen Original', img)
cv.imshow('Imagen Escalada', img_escalada)
cv.imshow('Imagen filtrada', filtrada)
cv.waitKey(0)
cv.destroyAllWindows()