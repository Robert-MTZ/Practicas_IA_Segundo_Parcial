# Practica_086_Reconocimiento_de_Objetos_E2_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Reconocimiento_de_Objetos

import cv2
import numpy as np
import tensorflow as tf

def cargar_modelo():
   
    # Cargamos el modelo pre-entrenado
    modelo = tf.keras.applications.EfficientNetB0(weights= imagenet, include_top=True)
    
    return modelo

def reconocer_objetos(imagen, modelo):
 
    # Normalizamos la imagen y la redimensionamos al tamaño esperado por el modelo
    imagen_preprocesada = tf.keras.applications.efficientnet.preprocess_input(imagen)
    imagen_preprocesada = tf.image.resize(imagen_preprocesada, (224, 224))
    imagen_preprocesada = np.expand_dims(imagen_preprocesada, axis=0)
    
    # Realizamos la inferencia con el modelo
    predicciones = modelo.predict(imagen_preprocesada)
    
    # Decodificamos las predicciones
    clases_decodificadas = tf.keras.applications.imagenet_utils.decode_predictions(predicciones)
    
    return clases_decodificadas[0]

# Cargamos el modelo pre-entrenado
modelo = cargar_modelo()

# Cargamos la imagen de ejemplo
imagen = cv2.imread(Ladrillos.jpg)
imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

# Reconocemos objetos en la imagen
objetos_detectados = reconocer_objetos(imagen, modelo)

# Imprimimos los objetos detectados y sus probabilidades
for objeto in objetos_detectados:
    print(Objeto: {objeto[1]}, Probabilidad: {objeto[2]})

# Mostramos la imagen con los objetos detectados
cv2.imshow(Objetos Detectados, cv2.cvtColor(imagen, cv2.COLOR_RGB2BGR))
cv2.waitKey(0)
cv2.destroyAllWindows()
