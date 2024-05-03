# Practica_070_Perceptron__ADALINE_y_MADALINE_E2_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria en Mecatronica

# Programa_Perceptron__ADALINE_y_MADALINE

import numpy as np # Genera numeros aleatorios y realizar calculos matriciales de manera eficiente

class Perceptron:
    def __init__(self, learning_rate=0.01, n_iterations=100):
        self.learning_rate = learning_rate  # Tasa de aprendizaje
        self.n_iterations = n_iterations    # Número de iteraciones de entrenamiento
        self.weights = None                 # Pesos sin entrenar

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features + 1)  # Inicializamos los pesos a cero, más un peso para el sesgo

        for _ in range(self.n_iterations):
            for idx, x_i in enumerate(X):
                y_pred = self.predict(x_i)          # Calculamos la predicción
                update = self.learning_rate * (y[idx] - y_pred)  # Calculamos el ajuste a los pesos
                self.weights[1:] += update * x_i    # Actualizamos los pesos de las características
                self.weights[0] += update           # Actualizamos el sesgo

    def predict(self, X):
        linear_output = np.dot(X, self.weights[1:]) + self.weights[0]  # Calculamos la salida lineal
        return np.where(linear_output >= 0, 1, 0)                     # Aplicamos la función de activación (Umbral)

class Adaline:
    def __init__(self, learning_rate=0.01, n_iterations=100):
        self.learning_rate = learning_rate  # Tasa de aprendizaje
        self.n_iterations = n_iterations    # Número de iteraciones de entrenamiento
        self.weights = None                 # Pesos sin entrenar

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features + 1)  # Inicializamos los pesos a cero, más un peso para el sesgo

        for _ in range(self.n_iterations):
            for idx, x_i in enumerate(X):
                y_pred = self.predict(x_i)          # Calculamos la predicción
                update = self.learning_rate * (y[idx] - y_pred)  # Calculamos el ajuste a los pesos
                self.weights[1:] += update * x_i    # Actualizamos los pesos de las características
                self.weights[0] += update           # Actualizamos el sesgo

    def predict(self, X):
        linear_output = np.dot(X, self.weights[1:]) + self.weights[0]  # Calculamos la salida lineal
        return linear_output                                            # No aplicamos función de activación (lineal)

class Madaline:
    def __init__(self, learning_rate=0.01, n_iterations=100, threshold=0.5):
        self.learning_rate = learning_rate  # Tasa de aprendizaje
        self.n_iterations = n_iterations    # Número de iteraciones de entrenamiento
        self.threshold = threshold          # Umbral de activación
        self.weights = None                 # Pesos sin entrenar

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features + 1)  # Inicializamos los pesos a cero, más un peso para el sesgo

        for _ in range(self.n_iterations):
            for idx, x_i in enumerate(X):
                y_pred = self.predict(x_i)          # Calculamos la predicción
                error = y[idx] - y_pred            # Calculamos el error
                update = self.learning_rate * error  # Calculamos el ajuste a los pesos
                self.weights[1:] += update * x_i    # Actualizamos los pesos de las características
                self.weights[0] += update           # Actualizamos el sesgo

    def predict(self, X):
        linear_output = np.dot(X, self.weights[1:]) + self.weights[0]  # Calculamos la salida lineal
        return np.where(linear_output >= self.threshold, 1, 0)        # Aplicamos la función de activación (Umbral)

