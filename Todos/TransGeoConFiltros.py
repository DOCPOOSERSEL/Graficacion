import cv2 as cv
import numpy as np

# Para imagen 1: escalar factor 2, aplicar filtro, rotar 40 , rotar 45 aplicar filtro
# Img 2: Escalar 2, rotar 45, aplicar filtro
# Img 2: Transladar imagen al centro, rotar 90 grados, escalar 2, aplicar filtro

#Crear condicion y ciclo para que decida cual filtro usar por pixel, recive la imagen y la regresa filtrada
def filtroBilineal (img,h,w):
    # Se crea la matriz del filtro de convolucion para tomar en cruz los pixeles para que se realce mejor la imagen y la de mas q ya estaba
    kernel_mas = np.array([[0, -1, 0],
                        [-1, 5, -1],
                        [0, -1, 0]])
    kernel_x = np.array([[-1,0,-1],
                    [0,5,0],
                    [-1,0,-1]])
    #Crear condicion y ciclo para que decida cual filtro usar por pixel
    for y in range(h):
        for x in range(w):
            # Toma los pixeles q estan al rededor de el pixel "Vecindad" 3*3
            vecindad = img[y:y+3, x:x+3]

            # Condición para seleccionar kernel checando que tan oscura es la region determinando cual usar sumandolos y dividiendo entre ellos
            if np.mean(vecindad) > 127:
                kernel = kernel_mas
            else:
                kernel = kernel_x

# Cargar la imagen en escala de grises
img = cv.imread('TsuruRojo.jpg', 0)
# Cordenadas para recorrer la img
h, w = img.shape

img_escalada = cv.resize(img, None, fx=2, fy=2)
# Se aplica el filtro y se usa el '-1' para que mantenga la misma profundidad que la imagen que fue escalada
filtrada = cv.filter2D(img_escalada,-1,kernel_x)

# Mostrar la imagen original y la escalada
cv.imshow('Imagen Original', img)
cv.imshow('Imagen Escalada', img_escalada)
cv.imshow('Imagen filtrada', filtrada)
cv.waitKey(0)
cv.destroyAllWindows()

#Ya va amarrando :)