# Practica_062_Algoritmo_EM_E2_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria en Mecatronica

# Programa_Algoritmo_EM

import numpy as np  # Genera numeros aleatorios y realizar calculos matriciales de manera eficiente
from scipy.stats import multivariate_normal # Puede generar muestras aleatorias de una distribución normal multivariada, calcular la función de densidad de probabilidad (PDF) en un punto dado

class GaussianMixtureEM:
    def __init__(self, n_components, max_iter=100, tol=1e-6):
        self.n_components = n_components  # Número de componentes (clusters)
        self.max_iter = max_iter  # Número máximo de iteraciones
        self.tol = tol  # Tolerancia para la convergencia
        self.means = None  # Medias de los componentes
        self.covs = None  # Covarianzas de los componentes
        self.weights = None  # Pesos de los componentes

    def fit(self, X):
        n_samples, n_features = X.shape
        # Inicialización aleatoria de las medias, covarianzas y pesos
        self.means = X[np.random.choice(n_samples, self.n_components, replace=False)]
        self.covs = [np.cov(X.T) for _ in range(self.n_components)]
        self.weights = np.ones(self.n_components) / self.n_components

        log_likelihood = None
        for _ in range(self.max_iter):
            # Paso E: Calcular las probabilidades posteriores de pertenencia a cada componente
            posteriors = self._expectation(X)
            
            # Paso M: Actualizar los parámetros del modelo
            self._maximization(X, posteriors)
            
            # Calcular la log-verosimilitud y verificar la convergencia
            new_log_likelihood = self._compute_log_likelihood(X)
            if log_likelihood is not None and abs(new_log_likelihood - log_likelihood) < self.tol:
                break
            log_likelihood = new_log_likelihood

    def _expectation(self, X):
        posteriors = np.zeros((X.shape[0], self.n_components)) # Crea una matriz de ceros llamada posteriors con una forma (número de muestras en X, número de componentes). Esta matriz se utilizará para almacenar las probabilidades posteriores de que cada muestra pertenezca a cada componente de la mezcla
        for i in range(self.n_components): # Inicia un bucle for que recorre cada componente de la mezcla
            posteriors[:, i] = self.weights[i] * multivariate_normal.pdf(X, mean=self.means[i], cov=self.covs[i]) # Calcula las probabilidades posteriores para cada muestra para el componente i de la mezcla. Esto se hace multiplicando el peso del componente (self.weights[i]) por la función de densidad de probabilidad multivariada (multivariate_normal.pdf) evaluada en las muestras X, utilizando la media (self.means[i]) y la matriz de covarianza (self.covs[i]) del componente i
        posteriors /= posteriors.sum(axis=1, keepdims=True) # Normaliza las probabilidades posteriores dividiendo cada fila de la matriz posteriors por la suma de las probabilidades posteriores a lo largo de las columnas (componentes)
        return posteriors # Devuelve la matriz posteriors, que contiene las probabilidades posteriores normalizadas para cada muestra y componente de la mezcla

    def _maximization(self, X, posteriors):
        total_weight = np.sum(posteriors, axis=0) # Calcula la suma de las probabilidades posteriores a lo largo de las muestras (filas) para cada componente de la mezcla. Esto da como resultado un vector de longitud igual al número de componentes en la mezcla, donde cada elemento representa la suma total de las probabilidades posteriores para ese componente
        self.weights = total_weight / len(X) # Actualiza los pesos de los componentes de la mezcla dividiendo la suma total de las probabilidades posteriores por el número total de muestras en X. Esto normaliza los pesos para que sumen 1

        self.means = np.dot(posteriors.T, X) / total_weight[:, np.newaxis] # Calcula las nuevas medias para cada componente de la mezcla. Esto se hace multiplicando las probabilidades posteriores transpuestas por X y dividiendo por el total de pesos para cada componente. El resultado es una matriz donde cada fila representa la media para un componente

        for i in range(self.n_components): # Inicia un bucle for que recorre cada componente de la mezcla
            diff = X - self.means[i] # Calcula la diferencia entre cada muestra y la media del componente i
            self.covs[i] = np.dot(posteriors[:, i] * diff.T, diff) / total_weight[i] # Actualiza las matrices de covarianza para cada componente de la mezcla. Esto se hace calculando la covarianza ponderada entre las diferencias entre las muestras y la media del componente. La covarianza se calcula utilizando las probabilidades posteriores y las diferencias entre las muestras y la media, y luego se divide por el total de pesos para el componente i

    def _compute_log_likelihood(self, X): # Esto define un método llamado _compute_log_likelihood dentro de una clase
        log_likelihood = 0 # Inicializa la variable log_likelihood a cero. Esta variable se utilizará para acumular el logaritmo de la verosimilitud de los datos
        for i in range(self.n_components): # Inicia un bucle for que recorre cada componente de la mezcla
            log_likelihood += self.weights[i] * multivariate_normal.pdf(X, mean=self.means[i], cov=self.covs[i]) # Para cada componente de la mezcla, calcula la contribución a la verosimilitud de los datos multiplicando el peso del componente por la probabilidad de las muestras X dadas las características (media y covarianza) del componente. Esto se hace utilizando la función de densidad de probabilidad multivariada multivariate_normal.pdf
        return np.log(log_likelihood).sum() # Calcula el logaritmo del total de la verosimilitud de los datos sumando los logaritmos de las contribuciones de cada componente. Esto se hace para evitar problemas numéricos asociados con la multiplicación de pequeños valores de probabilidad

X = np.random.randn(100, 2)  # Datos de ejemplo
model = GaussianMixtureEM(n_components=2)
model.fit(X)
print("Means:", model.means)
print("Covariances:", model.covs)
print("Weights:", model.weights)

