# Practica_084_Deteccion_de_Aristas_y_Segmentacion_E2_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Deteccion_de_Aristas_y_Segmentacion

import cv2
import numpy as np

def detectar_bordes(imagen):
    
    # Aplicamos el filtro Sobel para calcular la magnitud del gradiente en ambas direcciones (x e y)
    sobel_x = cv2.Sobel(imagen, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(imagen, cv2.CV_64F, 0, 1, ksize=3)
    
    # Calculamos la magnitud del gradiente
    magnitud_gradiente = np.sqrt(sobel_x**2 + sobel_y**2)
    
    # Aplicamos un umbral para segmentar la imagen en bordes y no bordes
    umbral = 50
    bordes = np.uint8(magnitud_gradiente > umbral) * 255
    
    return bordes

# Cargamos la imagen en escala de grises
imagen = cv2.imread("ejemplo.jpg", cv2.IMREAD_GRAYSCALE)

# Detectamos los bordes en la imagen
bordes_detectados = detectar_bordes(imagen)

# Mostramos la imagen original y la imagen con los bordes detectados
cv2.imshow("Imagen Original", imagen)
cv2.imshow("Bordes Detectados", bordes_detectados)

# Esperamos a que se presione una tecla y luego cerramos las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()
