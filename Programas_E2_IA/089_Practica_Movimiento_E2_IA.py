# Practica_089_Movimiento_E2_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Movimiento

import cv2

# Capturamos el video desde la cámara
captura = cv2.VideoCapture(0)

# Capturamos el primer fotograma
ret, primer_fotograma = captura.read()

# Convertimos el primer fotograma a escala de grises
primer_fotograma_gris = cv2.cvtColor(primer_fotograma, cv2.COLOR_BGR2GRAY)

while True:
    # Capturamos el siguiente fotograma
    ret, siguiente_fotograma = captura.read()
    
    # Convertimos el siguiente fotograma a escala de grises
    siguiente_fotograma_gris = cv2.cvtColor(siguiente_fotograma, cv2.COLOR_BGR2GRAY)
    
    # Calculamos la diferencia absoluta entre los dos fotogramas
    diferencia = cv2.absdiff(primer_fotograma_gris, siguiente_fotograma_gris)
    
    # Aplicamos un umbral para resaltar las áreas de cambio
    umbralizado = cv2.threshold(diferencia, 30, 255, cv2.THRESH_BINARY)[1]
    
    # Mostramos la imagen umbralizada
    cv2.imshow("Detección de Movimiento", umbralizado)
    
    # Actualizamos el fotograma inicial para la próxima iteración
    primer_fotograma_gris = siguiente_fotograma_gris
    
    # Esperamos a que se presione la tecla 'q' para salir del bucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberamos la captura y cerramos todas las ventanas
captura.release()
cv2.destroyAllWindows()

