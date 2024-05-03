# Practica_072_Redes_Multicapa_E2_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria en Mecatronica

# Programa_Redes_Multicapa

import tensorflow as tf
from tensorflow.keras import layers, models

# Definimos la arquitectura de la red neuronal
def build_model(input_shape):
    model = models.Sequential([
        layers.Dense(64, activation='relu', input_shape=input_shape),  # Capa oculta con 64 neuronas y función de activación ReLU
        layers.Dense(64, activation='relu'),                           # Otra capa oculta con 64 neuronas y función de activación ReLU
        layers.Dense(10, activation='softmax')                          # Capa de salida con 10 neuronas (una para cada clase) y función de activación softmax
    ])
    return model

# Creamos un conjunto de datos de ejemplo (MNIST)
mnist = tf.keras.datasets.mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Normalizamos los valores de píxeles al rango [0, 1]
train_images, test_images = train_images / 255.0, test_images / 255.0

# Construimos el modelo
model = build_model((28*28,))

# Compilamos el modelo
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Entrenamos el modelo
history = model.fit(train_images.reshape(-1, 28*28), train_labels, epochs=5, validation_data=(test_images.reshape(-1, 28*28), test_labels))

# Evaluamos el modelo con los datos de prueba
test_loss, test_acc = model.evaluate(test_images.reshape(-1, 28*28),  test_labels, verbose=2)
print('\nPrecisión del modelo en los datos de prueba:', test_acc)

