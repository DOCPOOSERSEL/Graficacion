import cv2 as cv

# Cargar la imagen
img = cv.imread('TsuruRojo.jpg', cv.IMREAD_GRAYSCALE)  # la convertimos a escala de grises

# Operador de Identidad
identidad = img.copy()

# Negativo de la imagen
negativo = 255 - img

# Umbralización
_, umbral = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

# Aumentar brillo
brillo = cv.add(img, 50)  # suma 50 a cada píxel

# 4. Reducir brillo
oscura = cv.subtract(img, 50)  # resta 50 a cada píxel

# Mostrar todas las imágenes
cv.imshow('Original', img)
cv.imshow('Identidad', identidad)
cv.imshow('Negativo', negativo)
cv.imshow('Umbral', umbral)
cv.imshow('Brillo mas', brillo)
cv.imshow('Brillo menos', oscura)

cv.waitKey(0)
cv.destroyAllWindows()