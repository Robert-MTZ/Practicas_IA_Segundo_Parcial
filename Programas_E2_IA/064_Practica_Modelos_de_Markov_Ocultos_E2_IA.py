# Practica_064_Modelos_de_Markov_Ocultos_E2_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria en Mecatronica

# Programa_Modelos_de_Markov_Ocultos

from hmmlearn import hmm #  biblioteca de Python que se utiliza para trabajar con modelos ocultos de Markov (HMM, por sus siglas en inglés). Los HMM son modelos estadísticos que se utilizan comúnmente para modelar secuencias de datos con estructura temporal, como el reconocimiento de voz, el procesamiento del lenguaje natural, el análisis de secuencias de ADN, entre otro
import numpy as np  # Genera numeros aleatorios y realizar calculos matriciales de manera eficiente

# Creamos un objeto HMM con 2 estados ocultos y 3 símbolos observables
model = hmm.MultinomialHMM(n_components=2, n_iter=100)

# Definimos las probabilidades iniciales de los estados ocultos
model.startprob_ = np.array([0.5, 0.5])  # Probabilidad inicial de cada estado oculto

# Definimos las probabilidades de transición entre los estados ocultos
model.transmat_ = np.array([[0.7, 0.3],  # Probabilidad de transición de estado 1 a estado 1 y estado 1 a estado 2
                            [0.4, 0.6]])  # Probabilidad de transición de estado 2 a estado 1 y estado 2 a estado 2

# Definimos las probabilidades de emisión de cada estado oculto para cada símbolo observable
model.emissionprob_ = np.array([[0.2, 0.3, 0.5],  # Probabilidad de observar cada símbolo dado el estado 1
                                [0.4, 0.4, 0.2]])  # Probabilidad de observar cada símbolo dado el estado 2

# Generamos una secuencia de observaciones
X, Z = model.sample(10)  # Generamos una secuencia de 10 observaciones y los estados ocultos correspondientes

# Imprimimos la secuencia de observaciones y los estados ocultos correspondientes
print("Secuencia de observaciones:")
print(X)
print("Estados ocultos correspondientes:")
print(Z)

# Ajustamos el modelo a la secuencia de observaciones
model.fit(X)

# Calculamos la probabilidad logarítmica de la secuencia de observaciones
log_prob = model.score(X)

print("Probabilidad logarítmica de la secuencia de observaciones:", log_prob)


