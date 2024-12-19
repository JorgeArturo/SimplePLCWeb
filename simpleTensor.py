#Adhiere librerias de tensorflow con matplot
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import tensorflow as tf
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Inicializa la cámara web
cap = cv2.VideoCapture(0)

# Carga el clasificador de Haar para detección de rostros
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    # Captura frame por frame
    ret, frame = cap.read()
    
    # Convierte la imagen a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detecta rostros en la imagen
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    # Dibuja un rectángulo alrededor de cada rostro
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    # Muestra el frame resultante
    cv2.imshow('frame', frame)
    
    # Sale del bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera la captura y cierra las ventanas
cap.release()
cv2.destroyAllWindows()
