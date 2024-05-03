# Practica_069_Funciones_de_Activacion_E2_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria en Mecatronica

# Programa_Funciones_de_Activacion

import numpy as np # Genera numeros aleatorios y realizar calculos matriciales de manera eficiente

# Función de activación Sigmoide
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Función de activación ReLU (Rectified Linear Unit)
def relu(x):
    return np.maximum(0, x)

# Función de activación Tangente Hiperbólica
def tanh(x):
    return np.tanh(x)

# Datos de ejemplo
x = np.array([-1, 0, 1])

# Aplicamos cada función de activación a los datos de ejemplo
sigmoid_output = sigmoid(x)
relu_output = relu(x)
tanh_output = tanh(x)

# Imprimimos los resultados
print("Datos de entrada:", x)
print("Resultado de la función sigmoide:", sigmoid_output)
print("Resultado de la función ReLU:", relu_output)
print("Resultado de la función tangente hiperbólica:", tanh_output)
