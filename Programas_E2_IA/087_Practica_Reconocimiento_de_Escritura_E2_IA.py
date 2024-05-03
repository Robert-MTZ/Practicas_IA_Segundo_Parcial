# Practica_087_Reconocimiento_de_Escritura_E2_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Reconocimiento_de_Escritura

import tensorflow as tf

# Cargamos el conjunto de datos MNIST
mnist = tf.keras.datasets.mnist
(x_entrenamiento, y_entrenamiento), (x_prueba, y_prueba) = mnist.load_data()

# Normalizamos los valores de píxeles de las imágenes al rango [0, 1]
x_entrenamiento, x_prueba = x_entrenamiento / 255.0, x_prueba / 255.0

# Definimos el modelo de red neuronal convolucional (CNN)
modelo = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),  # Capa de aplanamiento para convertir la imagen 2D en un vector 1D
    tf.keras.layers.Dense(128, activation='relu'),  # Capa densa con activación ReLU
    tf.keras.layers.Dropout(0.2),  # Capa de dropout para regularización
    tf.keras.layers.Dense(10, activation='softmax')  # Capa de salida con activación softmax para clasificación multiclase
])

# Compilamos el modelo
modelo.compile(optimizer='adam',
               loss='sparse_categorical_crossentropy',
               metrics=['accuracy'])

# Entrenamos el modelo
modelo.fit(x_entrenamiento, y_entrenamiento, epochs=5)

# Evaluamos el modelo con los datos de prueba
puntuacion = modelo.evaluate(x_prueba, y_prueba)
print("Precisión en los datos de prueba:", puntuacion[1])
