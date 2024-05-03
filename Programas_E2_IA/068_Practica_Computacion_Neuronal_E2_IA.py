# Practica_068_Computacion_Neuronal_E2_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria en Mecatronica

# Programa_Computacion_Neuronal

import numpy as np # Genera numeros aleatorios y realizar calculos matriciales de manera eficiente

# Definimos la función de activación sigmoide
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Definimos los datos de entrada
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

# Definimos los datos de salida esperados
y = np.array([[0], [1], [1], [0]])

# Inicializamos los pesos de forma aleatoria
np.random.seed(0)
weights_input_hidden = np.random.rand(2, 2)  # Pesos para la capa de entrada a la capa oculta
weights_hidden_output = np.random.rand(2, 1)  # Pesos para la capa oculta a la capa de salida

# Definimos el número de épocas de entrenamiento
epochs = 10000

# Definimos la tasa de aprendizaje
learning_rate = 0.1

# Entrenamiento de la red neuronal
for epoch in range(epochs):
    # Propagación hacia adelante (forward propagation)
    hidden_layer_input = np.dot(X, weights_input_hidden)
    hidden_layer_output = sigmoid(hidden_layer_input)
    output_layer_input = np.dot(hidden_layer_output, weights_hidden_output)
    output = sigmoid(output_layer_input)

    # Cálculo del error
    error = y - output

    # Propagación hacia atrás (backpropagation) y actualización de los pesos
    d_output = error * (output * (1 - output))
    error_hidden_layer = np.dot(d_output, weights_hidden_output.T)
    d_hidden_layer = error_hidden_layer * (hidden_layer_output * (1 - hidden_layer_output))

    weights_hidden_output += np.dot(hidden_layer_output.T, d_output) * learning_rate
    weights_input_hidden += np.dot(X.T, d_hidden_layer) * learning_rate

# Imprimimos los pesos finales de la red neuronal
print("Pesos finales de la capa de entrada a la capa oculta:")
print(weights_input_hidden)
print("\nPesos finales de la capa oculta a la capa de salida:")
print(weights_hidden_output)

# Hacemos predicciones con la red neuronal entrenada
print("\nPredicciones después del entrenamiento:")
print(output)

