# Practica_074_Mapas_Autoorganizados_de_Kohonen_E2_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Mapas_Autoorganizados_de_Kohonen

import numpy as np # Genera numeros aleatorios y realizar calculos matriciales de manera eficiente
import matplotlib.pyplot as plt

class KohonenMap:
    def __init__(self, input_dim, output_dim, learning_rate=0.1, sigma=1.0):
        self.input_dim = input_dim  # Dimensión de los datos de entrada
        self.output_dim = output_dim  # Dimensión de la capa de salida (mapa)
        self.learning_rate = learning_rate  # Tasa de aprendizaje
        self.sigma = sigma  # Parámetro de vecindad inicial
        
        # Inicializamos los pesos de forma aleatoria
        self.weights = np.random.rand(output_dim[0], output_dim[1], input_dim)
        
        # Creamos una cuadrícula de neuronas
        self.neuron_grid = np.array([[np.array([i, j]) for j in range(output_dim[1])] for i in range(output_dim[0])])

    def train(self, data, epochs):
        for epoch in range(epochs):
            for idx, x in enumerate(data):
                # Encuentra la neurona ganadora (BMU - Best Matching Unit)
                bmu_idx = self.find_bmu(x)

                # Actualiza los pesos de las neuronas vecinas
                self.update_neighborhood(bmu_idx, x, epoch, epochs)

    def find_bmu(self, x):
        # Calcula la distancia euclidiana entre el vector de entrada y los pesos de todas las neuronas
        distances = np.linalg.norm(self.weights - x, axis=-1)
        
        # Encuentra el índice de la neurona con la distancia mínima (la neurona ganadora)
        bmu_idx = np.unravel_index(np.argmin(distances), distances.shape)
        return bmu_idx

    def update_neighborhood(self, bmu_idx, x, epoch, max_epochs):
        # Calcula el radio de la vecindad (disminuye con el tiempo)
        neighborhood_radius = self.sigma * np.exp(-epoch / max_epochs)
        
        # Calcula la influencia de la neurona ganadora en las neuronas vecinas
        influence = np.exp(-np.linalg.norm(self.neuron_grid - bmu_idx, axis=-1) / (2 * neighborhood_radius))
        
        # Actualiza los pesos de las neuronas vecinas
        for i in range(self.output_dim[0]):
            for j in range(self.output_dim[1]):
                distance = np.linalg.norm(np.array([i, j]) - np.array(bmu_idx))
                if distance <= neighborhood_radius:
                    self.weights[i, j] += influence[i, j] * self.learning_rate * (x - self.weights[i, j])

    def visualize_map(self, data):
        plt.figure(figsize=(10, 8))
        for x in data:
            bmu_idx = self.find_bmu(x)
            plt.plot(bmu_idx[1], bmu_idx[0], marker='o', markersize=8, markerfacecolor='None', markeredgecolor='r')
        plt.title('Mapa Autoorganizado de Kohonen')
        plt.xlabel('Índice en X')
        plt.ylabel('Índice en Y')
        plt.grid()
        plt.show()

# Datos de ejemplo
data = np.random.rand(100, 2)  # Generamos 100 puntos en un espacio bidimensional

# Creamos una instancia del mapa de Kohonen con una capa de salida de 10x10 neuronas
map_dim = (10, 10)
kmap = KohonenMap(input_dim=2, output_dim=map_dim, learning_rate=0.1, sigma=3.0)

# Entrenamos el mapa de Kohonen
kmap.train(data, epochs=100)

# Visualizamos el mapa
kmap.visualize_map(data)

