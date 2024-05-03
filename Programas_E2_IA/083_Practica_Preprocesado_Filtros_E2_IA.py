# Practica_083_Preprocesado_Filtros_E2_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Preprocesado_Filtros

import cv2
import numpy as np

def aplicar_filtro_gaussiano(imagen):

    # Aplicamos el filtro gaussiano con un kernel de 5x5 y una desviación estándar de 0
    imagen_suavizada = cv2.GaussianBlur(imagen, (5, 5), 0)
    
    return imagen_suavizada

# Cargamos la imagen
imagen = cv2.imread("ejemplo.jpg")

# Aplicamos el filtro gaussiano
imagen_suavizada = aplicar_filtro_gaussiano(imagen)

# Mostramos la imagen original y la suavizada
cv2.imshow("Imagen Original", imagen)
cv2.imshow("Imagen Suavizada", imagen_suavizada)

# Esperamos a que se presione una tecla y luego cerramos las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()

