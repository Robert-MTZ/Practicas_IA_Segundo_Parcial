# Practica_088_Etiquetados_de_Líneas
_E2_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Etiquetados_de_Líneas


import cv2
import numpy as np

# Cargamos la imagen en escala de grises
imagen = cv2.imread(Ladrillos.jpg, cv2.IMREAD_GRAYSCALE)

# Aplicamos un umbral para obtener una imagen binaria
_, umbralizada = cv2.threshold(imagen, 128, 255, cv2.THRESH_BINARY)

# Buscamos contornos en la imagen umbralizada
contornos, _ = cv2.findContours(umbralizada, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Etiquetamos las líneas encontradas con números únicos
for i, contorno in enumerate(contornos):
    # Obtenemos el rectángulo delimitador del contorno
    x, y, w, h = cv2.boundingRect(contorno)
    # Dibujamos el rectángulo delimitador en la imagen original
    cv2.rectangle(imagen, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # Etiquetamos el contorno con un número único y lo mostramos en la imagen
    cv2.putText(imagen, str(i + 1), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

# Mostramos la imagen con las líneas etiquetadas
cv2.imshow(Imagen con líneas etiquetadas, imagen)

# Esperamos a que se presione una tecla y luego cerramos la ventana
cv2.waitKey(0)
cv2.destroyAllWindows()

