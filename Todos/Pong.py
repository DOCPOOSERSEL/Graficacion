import cv2 as cv
import numpy as np

# Se necesita guardar las posiciones de la ventana y velocidad para cambiar la direccion
# Tamaño de la ventana
W, H = 500, 500  
# Posición inicial
x, y = 50, 50  
# Velocidad es sobre donde vamos a efectuar el cambio de direccion
# Tambien depende de si cambiamos la velocidad el angulo del rebote para evitar que repita el mismo rebote si es muy similar
# Ej x=5 y y=5 repite el mismo patron que es una linea forma \
dx, dy = 4, 5  

while True:
    img = np.ones((H, W, 3), dtype=np.uint8) * 255
    cv.circle(img, (x, y), 20, (0, 234, 21), -1)
    x += dx
    y += dy

    # Rebote en los bordes, esto checa que si en 20 sale de los bordes se le resta la velocidad da 0
    # Pero sigue restando hasta que sale hacia otro lado
    if x - 20 <= 0 or x + 20 >= W:
        dx = -dx
    if y - 20 <= 0 or y + 20 >= H:
        dy = -dy

    cv.imshow("Pelota rebotando", img)

   
    k = cv.waitKey(20) & 0xFF
    if k == ord('q'):
        break

cv.destroyAllWindows()

 