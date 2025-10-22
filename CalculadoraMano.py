import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5)
ancho_cuadro = 640 // 10
ancho_cuadro_op = 640 // 4
alto_cuadro = 60
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame= cv2.flip(frame, 1)
    # Convertir imagen a RGB (MediaPipe usa RGB)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    # Variables para guardar coordenadas
    left_index = None
    right_index = None

    

    if results.multi_hand_landmarks and results.multi_handedness:
        for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
            label = handedness.classification[0].label  # 'Left' o 'Right'
            #print(label)
            h, w, _ = frame.shape

            # Coordenadas del índice (landmark 8)
            index_tip = hand_landmarks.landmark[8]
            x, y = int(index_tip.x * w), int(index_tip.y * h)

            # Guardar según la mano
            if label == 'Left':
                left_index = (x, y)
            elif label == 'Right':
                right_index = (x, y)


        # Si ambas manos detectadas, dibujar línea entre los dos puntos
        if left_index and right_index:
            cv2.line(frame, left_index, right_index, (0, 255, 0), 3)
            cv2.circle(frame, left_index, 8, (255, 0, 0), -1)
            cv2.circle(frame, right_index, 8, (0, 0, 255), -1)

    for i in range(10):
        x_inicio = i * ancho_cuadro
        x_fin = (i + 1) * ancho_cuadro
        cv2.rectangle(frame, (x_inicio, 0), (x_fin, alto_cuadro), (0,0,225), 0)
    for i in range(4):
        x_inicio = i * ancho_cuadro_op
        x_fin = (i + 1) * ancho_cuadro_op
        cv2.rectangle(frame, (x_inicio, 400), (x_fin, alto_cuadro+419), (0,0,225), 0) 

    cv2.imshow("Line", frame)
    #Dibuja los cuadrados   


    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()