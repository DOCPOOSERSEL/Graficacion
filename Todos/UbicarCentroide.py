import numpy as np   # Importa la librería NumPy, útil para trabajar con arreglos y operaciones numéricas.
import cv2 as cv     # Importa la librería OpenCV, que se utiliza para procesamiento de imágenes.
import imutuls

# Crea una imagen de 500x500 píxeles, todos con valor 240 (gris claro). 
# La imagen tiene solo un canal (escala de grises) y está inicializada con valores de tipo uint8 (enteros sin signo de 8 bits).
img = np.ones((500, 500), dtype=np.uint8) * 240

# Modifica algunos píxeles específicos en las coordenadas (30, 30) a (30, 35) para que tengan un valor de 1 (casi negro).
# Esto creará una pequeña línea vertical de 6 píxeles en la imagen de color casi negro.
img[30, 30] = 1
img[30, 31] = 1
img[30, 32] = 1
img[30, 33] = 1
img[30, 34] = 1
img[30, 35] = 1

# Preparar la imagen para el metodo
img = cv.imread('data\\left.png')
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# Rango para color negro en HSV
lower_black = np.array([0, 0, 0])
upper_black = np.array([180, 255, 50]) # valor máximo de V bajo, para que sea negro

# Crear máscara para negro
black = cv.inRange(hsv, lower_black, upper_black)

# Encuentra los contornos y los pone en una forma de lista para realizar operaciones en base a estos 
cnts1 = cv.findContours(black,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
cnts1 = imutuls.grab_contours(cnts1)

for c in cnts1:  # cnts1 es la lista de contornos detectados
    M = cv.moments(c)  # Calcula los momentos del contorno, (son propiedades geométricas)
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"]) 
        cY = int(M["m01"] / M["m00"]) 
    else:
        cX, cY = 0, 0  # Evita división por cero si el contorno es muy pequeño
    
# Aquí cX y cY son las coordenadas del centro del contorno

# Muestra la imagen en una ventana con el título 'img'. 
cv.imshow('img', img)

# Espera a que el usuario presione cualquier tecla para continuar.
cv.waitKey()

# Cierra todas las ventanas creadas por OpenCV.
cv.destroyAllWindows()