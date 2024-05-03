# Practica_073_Retropropagacion_del_Error_E2_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Retropropagacion_del_Error

import numpy as np # Genera numeros aleatorios y realizar calculos matriciales de manera eficiente

class NeuralNetwork:
    def __init__(self, layers, learning_rate=0.1):
        self.layers = layers  # Número de neuronas en cada capa
        self.num_layers = len(layers)  # Número de capas en la red
        self.learning_rate = learning_rate  # Tasa de aprendizaje
        self.weights = [np.random.randn(layers[i], layers[i-1]) for i in range(1, self.num_layers)]  # Inicializamos los pesos de forma aleatoria
        self.biases = [np.random.randn(layers[i]) for i in range(1, self.num_layers)]  # Inicializamos los sesgos de forma aleatoria

    def feedforward(self, X):
        a = X
        for w, b in zip(self.weights, self.biases):
            a = sigmoid(np.dot(w, a) + b)  # Aplicamos la función de activación (sigmoid) en cada capa
        return a

    def backpropagation(self, X, y):
        # Inicializamos listas para almacenar las derivadas de los pesos y sesgos
        dW = [np.zeros(w.shape) for w in self.weights]
        dB = [np.zeros(b.shape) for b in self.biases]
        
        # Feedforward
        activation = X
        activations = [X]  # Lista para almacenar las activaciones en cada capa
        zs = []  # Lista para almacenar las entradas ponderadas en cada capa
        
        for w, b in zip(self.weights, self.biases):
            z = np.dot(w, activation) + b
            zs.append(z)
            activation = sigmoid(z)
            activations.append(activation)
        
        # Backpropagation
        delta = self.cost_derivative(activations[-1], y) * sigmoid_prime(zs[-1])
        dW[-1] = np.dot(delta, activations[-2].T)
        dB[-1] = delta
        
        for l in range(2, self.num_layers):
            z = zs[-l]
            sp = sigmoid_prime(z)
            delta = np.dot(self.weights[-l+1].T, delta) * sp
            dW[-l] = np.dot(delta, activations[-l-1].T)
            dB[-l] = delta
        
        return (dW, dB)

    def train(self, X, y, epochs, batch_size):
        n = len(X)
        for i in range(epochs):
            # Barajamos los datos
            indices = np.random.permutation(n)
            X_shuffled = X[indices]
            y_shuffled = y[indices]

            for j in range(0, n, batch_size):
                # Obtenemos el lote actual
                X_batch = X_shuffled[j:j+batch_size]
                y_batch = y_shuffled[j:j+batch_size]

                # Calculamos las derivadas de los pesos y sesgos utilizando el algoritmo de backpropagation
                dW = [np.zeros(w.shape) for w in self.weights]
                dB = [np.zeros(b.shape) for b in self.biases]
                for x, y_true in zip(X_batch, y_batch):
                    delta_dW, delta_dB = self.backpropagation(x, y_true)
                    dW = [nw+dnw for nw, dnw in zip(dW, delta_dW)]
                    dB = [nb+dnb for nb, dnb in zip(dB, delta_dB)]

                # Actualizamos los pesos y sesgos utilizando el descenso de gradiente estocástico
                self.weights = [w - (self.learning_rate / batch_size) * nw for w, nw in zip(self.weights, dW)]
                self.biases = [b - (self.learning_rate / batch_size) * nb for b, nb in zip(self.biases, dB)]

    def cost_derivative(self, output_activations, y):
        return output_activations - y

def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))

def sigmoid_prime(z):
    return sigmoid(z) * (1 - sigmoid(z))

# Datos de ejemplo (puertas lógicas OR)
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [1]])

# Creamos una red neuronal con una capa oculta de 2 neuronas
network = NeuralNetwork([2, 2, 1], learning_rate=0.5)

# Entrenamos la red neuronal
network.train(X.T, y.T, epochs=10000, batch_size=4)

# Evaluamos la red neuronal con los datos de entrada
for x, y_true in zip(X, y):
    prediction = network.feedforward(x.reshape(-1, 1))
    print("Entrada:", x, "Predicción:", prediction, "Etiqueta verdadera:", y_true)

