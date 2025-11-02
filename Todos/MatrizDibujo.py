import numpy as np
import cv2 as cv

# Crear imagen de 50x50 píxeles, fondo blanco
img = np.ones((50, 50), dtype=np.uint8) * 255

# Cabeza (3x3 píxeles)
img[9:12, 24:27] = 0

# Cuerpo (4 píxeles vertical)
img[12:16, 25] = 0

# Brazos
img[13, 23] = 0
img[13, 27] = 0

# Piernas
img[16, 24] = 0
img[16, 26] = 0
img[17, 23] = 0
img[17, 27] = 0

# Mostrar imagen
cv.imshow('Monito de palo', img)
cv.waitKey(0)
cv.destroyAllWindows()
