# Practica_063_Agrupamiento_No_Supervisado_E2_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria en Mecatronica

# Programa_Agrupamiento_No_Supervisado

import numpy as np # Genera numeros aleatorios y realizar calculos matriciales de manera eficiente

class KMeans:
    def __init__(self, n_clusters, max_iter=300):
        self.n_clusters = n_clusters  # Número de clústeres
        self.max_iter = max_iter  # Número máximo de iteraciones
        self.centroids = None  # Centroides de los clústeres

    def fit(self, X):
        # Inicialización aleatoria de los centroides
        self.centroids = X[np.random.choice(X.shape[0], self.n_clusters, replace=False)]
        
        for _ in range(self.max_iter):
            # Asignación de cada punto al clúster más cercano
            labels = self._assign_clusters(X)
            
            # Actualización de los centroides
            new_centroids = self._update_centroids(X, labels)
            
            # Verificar la convergencia
            if np.allclose(new_centroids, self.centroids):
                break
            
            self.centroids = new_centroids

    def _assign_clusters(self, X):
        # Calcula la distancia entre cada punto y cada centroide
        distances = np.sqrt(((X[:, np.newaxis] - self.centroids) ** 2).sum(axis=2))
        # Asigna cada punto al clúster más cercano
        return np.argmin(distances, axis=1)

    def _update_centroids(self, X, labels):
        new_centroids = np.zeros_like(self.centroids)
        # Calcula el nuevo centroide de cada clúster como el promedio de los puntos asignados a él
        for i in range(self.n_clusters):
            new_centroids[i] = np.mean(X[labels == i], axis=0)
        return new_centroids

X = np.random.rand(100, 2)  # Datos de ejemplo
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)
print("Centroides finales:")
print(kmeans.centroids)
