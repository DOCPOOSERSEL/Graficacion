import cv2
import numpy as np

# Tamaño de la imagen
alto, ancho = 600, 600

# Parámetro t
t = np.linspace(0, 2*np.pi, 500)

# Función que devuelve las 10 curvas
def ecuaciones(t):
    curvas = []
    # Cada curva se ajusta 
    curvas.append( (np.cos(t)*100 + 300, np.sin(t)*100 + 300) )   # 1. Círculod
    curvas.append( (2*np.cos(t)*50 + 300, np.sin(t)*100 + 300) )  # 2. Elipse
    curvas.append( (np.cos(t)/(1+np.sin(t)**2)*150 + 300, np.cos(t)*np.sin(t)/(1+np.sin(t)**2)*150 + 300) ) # 3. Lemniscata
    curvas.append( (np.sin(2*t)*100 + 300, np.sin(3*t)*100 + 300) ) # 4. Hipocicloide simple
    curvas.append( (np.sin(3*t)*50 + 300, np.sin(3*t)*50 + 300) )   # 5. Pétalo
    curvas.append( (np.sin(t)*100 + 300, np.sin(2*t)*100 + 300) )   # 6. Variante 1
    curvas.append( (np.cos(t)*100 + 300, np.cos(3*t)*100 + 300) )   # 7. Variante 2
    curvas.append( (np.sin(t)*100 + 300, np.sin(2*t)*50 + 300) )    # 8. Variante 3
    curvas.append( (np.cos(2*t)*50 + 300, np.sin(3*t)*100 + 300) )  # 9. Variante 4
    curvas.append( (np.sin(3*t)*100 + 300, np.cos(2*t)*50 + 300) )  # 10. Variante 5
    return curvas

curvas = ecuaciones(t)

# Dibujar cada curva en su propia imagen
for idx, (x_vals, y_vals) in enumerate(curvas):
    img = np.ones((alto, ancho, 3), dtype=np.uint8) * 255  # Fondo blanco
    x_pts = np.clip(np.array(x_vals, dtype=np.int32), 0, ancho-1)   # Asegura que queden dentro
    y_pts = np.clip(np.array(y_vals, dtype=np.int32), 0, alto-1)

    for i in range(len(x_pts)-1):
        cv2.line(img, (x_pts[i], y_pts[i]), (x_pts[i+1], y_pts[i+1]), (0,0,0), 1)

    cv2.imshow(str(idx+1), img)

cv2.waitKey(0)
cv2.destroyAllWindows()
