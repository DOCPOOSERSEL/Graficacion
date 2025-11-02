import cv2 as cv 
import random as r

rostro = cv.CascadeClassifier('haarcascade_frontalface_alt2.xml')
cap = cv.VideoCapture(0)
# VAriables para el movimiento de los ojos y lengua guarda la direccion y controla las pupilas
dx = 0
direccion = 1
# Guarda la dirrecion de la lengua y la otra controla el movimiento
dx_lengua = 0
direccion_lengua = 1


while True:
    ret, img = cap.read()
    gris = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    rostros = rostro.detectMultiScale(gris, 1.3, 5)
    for(x,y,w,h) in rostros:
        res = int((w+h)/8)
        img = cv.rectangle(img, (x,y), (x+w, y+h), (234, 23,23), 5)
        img = cv.rectangle(img, (x,int(y+h/2)), (x+w, y+h), (0,255,0),5 )
        
        # Ojos y pupilas 
        img = cv.circle(img, (x + int(w*0.3), y + int(h*0.4)) , w//10, (0, 0, 0), 2 ) #Operacion con w// para q de enteros y se cambie de tamaño
        img = cv.circle(img, (x + int(w*0.7), y + int(h*0.4)) , w//10, (0, 0, 0), 2 )
        img = cv.circle(img, (x + int(w*0.3), y + int(h*0.4)) , w//11, (255, 255, 255), -1 )
        img = cv.circle(img, (x + int(w*0.7), y + int(h*0.4)) , w//11, (255, 255, 255), -1 )
        
        # If para que cheque las pupilas que se muevan
        if r.randint(0,10) == 1:# Randomise el cambio de lado se estan moviendo
            direccion *= -1
        dx += direccion
        if abs(dx) > w//25:  # Para q no se salga del width de los ojos uno mas chico
            direccion *= -1

        img = cv.circle(img, (x + int(w*0.3)+ dx, y + int(h*0.4)) , w//30, (0, 0, 255), -1 )
        img = cv.circle(img, (x + int(w*0.7)+ dx, y + int(h*0.4)) , w//30, (0, 0, 255), -1 )
        
        #Parpados y mi triste intendo de una funcion random que ya no me acorde y no tengo internet
        if r.randint(0,30) == 2:
            img = cv.circle(img, (x + int(w*0.3), y + int(h*0.4)) , w//10, (0, 0, 0), -1 )
            img = cv.circle(img, (x + int(w*0.7), y + int(h*0.4)) , w//10, (0, 0, 0), -1 )

        #Boca y lengua
        img = cv.circle(img, (x + int(w*0.5), y+75 + int(h*0.4)) , w//10, (0, 0, 0), -1 )
        # Movimiento de lengua lateral la neta no se porque lo meti en el for el if aumenta y decrementa para el movimiento
        # Cambia al azar a que lado se mueve la lengua como los ojos
        if r.randint(0, 10) == 1:
            direccion_lengua *= -1
        dx_lengua += direccion_lengua
        if abs(dx_lengua) > 7:  # límite de movimiento de la lengua para que no salga ni derecha ni izquierda toma el lado contrario
            direccion_lengua *= -1
        img = cv.line(img,(x + int(w * 0.5), y + 60 + int(h * 0.5)),(x + int(w * 0.5) + dx_lengua, y + 100 + int(h * 0.5)),(0, 0, 255),15)
    
    cv.imshow('img', img)
    if cv.waitKey(1)== ord('q'):
        break
    
cap.release
cv.destroyAllWindows()