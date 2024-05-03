# Practica_067_Aprendizaje_Profundo_Deep_Learning_E2_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria en Mecatronica

# Programa_Aprendizaje_Profundo_Deep_Learning

import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt

# Descargamos y cargamos el conjunto de datos CIFAR-10, que contiene 60,000 imágenes de 32x32 píxeles en 10 clases diferentes
(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()

# Normalizamos los valores de píxeles al rango [0, 1]
train_images, test_images = train_images / 255.0, test_images / 255.0

# Definimos el modelo de la red neuronal convolucional
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10)
])

# Compilamos el modelo
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# Entrenamos el modelo
history = model.fit(train_images, train_labels, epochs=10, 
                    validation_data=(test_images, test_labels))

# Evaluamos el modelo con los datos de prueba
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
print('\nPrecisión del modelo en los datos de prueba:', test_acc)

# Graficamos la precisión de entrenamiento y validación a lo largo de las épocas
plt.plot(history.history['accuracy'], label='Precisión de entrenamiento')
plt.plot(history.history['val_accuracy'], label = 'Precisión de validación')
plt.xlabel('Épocas')
plt.ylabel('Precisión')
plt.legend(loc='lower right')
plt.show()

