# Practica_065_k_NN_k_Medias_Clustering_E2_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria en Mecatronica

# Programa_k-NN_k-Medias_Clustering

from sklearn.datasets import make_blobs # Se utiliza para generar conjuntos de datos de ejemplo para problemas de clasificación y clustering
from sklearn.neighbors import KNeighborsClassifier # KNeighborsClassifier es una clase de scikit-learn que implementa el algoritmo k-NN (k-Nearest Neighbors) para clasificacion
from sklearn.cluster import KMeans # KMeans es una clase de scikit-learn que implementa el algoritmo k-Means para clustering
import matplotlib.pyplot as plt # Es una biblioteca de Python para la visualización de datos

# Creamos un conjunto de datos de ejemplo con 100 muestras y 2 características, y 3 clústeres
X, y = make_blobs(n_samples=100, centers=3, n_features=2, random_state=42)

# Visualizamos los datos de ejemplo
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis')
plt.title("Datos de ejemplo")
plt.xlabel("Característica 1")
plt.ylabel("Característica 2")
plt.show()

# Algoritmo k-NN
# Creamos un clasificador k-NN con k=3
knn = KNeighborsClassifier(n_neighbors=3)
# Ajustamos el clasificador a los datos de ejemplo
knn.fit(X, y)

# Generamos nuevos puntos de prueba
X_test = [[-2, 2], [0, 0], [2, -2]]
# Realizamos predicciones para los nuevos puntos de prueba
predictions_knn = knn.predict(X_test)

print("Predicciones k-NN:", predictions_knn)

# Algoritmo k-Means
# Creamos un modelo de k-Means con 3 clústeres
kmeans = KMeans(n_clusters=3, random_state=42)
# Ajustamos el modelo a los datos de ejemplo
kmeans.fit(X)

# Obtenemos las etiquetas de clúster asignadas a cada muestra
labels_kmeans = kmeans.labels_

# Visualizamos los clústeres encontrados por k-Means
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=labels_kmeans, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], marker='x', s=200, c='red', label='Centroides')
plt.title("Clústeres encontrados por k-Means")
plt.xlabel("Característica 1")
plt.ylabel("Característica 2")
plt.legend()
plt.show()

print("Etiquetas de clúster asignadas por k-Means:", labels_kmeans)

