# Practica_085_Texturas_y_Sombras_E2_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Texturas_y_Sombras

import cv2
import numpy as np

def detectar_texturas(imagen):

    # Aplicamos la transformada de Fourier a la imagen
    fft = np.fft.fft2(imagen)
    fft_shift = np.fft.fftshift(fft)
    magnitud_fft = np.log(np.abs(fft_shift))
    
    return magnitud_fft

def segmentar_sombras(imagen):

    # Aplicamos un umbral para detectar áreas con sombras
    umbral = 100
    _, sombras = cv2.threshold(imagen, umbral, 255, cv2.THRESH_BINARY)
    
    return sombras

# Cargamos la imagen en escala de grises
imagen = cv2.imread(ladrillos.jpg, cv2.IMREAD_GRAYSCALE)

# Detectamos texturas en la imagen
texturas_detectadas = detectar_texturas(imagen)

# Segmentamos áreas con sombras en la imagen
areas_sombras = segmentar_sombras(imagen)

# Mostramos la imagen original, las texturas detectadas y las áreas de sombras segmentadas
cv2.imshow("Imagen Original", imagen)
cv2.imshow("Texturas Detectadas", texturas_detectadas)
cv2.imshow("Áreas de Sombras", areas_sombras)

# Esperamos a que se presione una tecla y luego cerramos las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()
  
