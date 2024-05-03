# Practica_055_Algoritmo_Hacia_Delante_Atras_E2_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria en Mecatronica

# Programa_Algoritmo_Hacia_Delante_Atras

import numpy as np # Genera numeros aleatorios y realizar calculos matriciales de manera eficiente

class HMM:
    def __init__(self, A, B, pi):
       
        self.A = np.array(A)
        self.B = np.array(B)
        self.pi = np.array(pi)
        self.N = len(pi)
        self.M = len(B[0])
    
    def forward_backward(self, secuencia_observaciones):
       
        T = len(secuencia_observaciones)
        
        # Paso hacia delante
        alpha = np.zeros((T, self.N))
        alpha[0] = self.pi * self.B[:, secuencia_observaciones[0]]
        for t in range(1, T):
            alpha[t] = np.dot(alpha[t-1], self.A) * self.B[:, secuencia_observaciones[t]]
        
        # Paso hacia atrás
        beta = np.ones((T, self.N))
        for t in reversed(range(T-1)):
            beta[t] = np.dot(self.A * self.B[:, secuencia_observaciones[t+1]], beta[t+1])
        
        # Cálculo de gamma y xi
        gamma = alpha * beta / np.sum(alpha * beta, axis=1, keepdims=True)
        xi = np.zeros((T-1, self.N, self.N))
        for t in range(T-1):
            xi[t] = (alpha[t].reshape(-1, 1) * self.A * self.B[:, secuencia_observaciones[t+1]] * beta[t+1]) / np.sum(alpha[t] * beta[t])
        
        return gamma, xi

# Parámetros del HMM
A = [[0.7, 0.3],
     [0.4, 0.6]]  # Matriz de transición de estado
B = [[0.1, 0.4, 0.5],
     [0.6, 0.3, 0.1]]  # Matriz de emisión
pi = [0.6, 0.4]  # Distribución inicial de estado

# Creamos una instancia del HMM
hmm = HMM(A, B, pi)

# Secuencia de observaciones
secuencia_observaciones = [0, 1, 2, 0, 2]

# Ejecutamos el algoritmo de Hacia Delante-Atrás
gamma, xi = hmm.forward_backward(secuencia_observaciones)

# Imprimimos las probabilidades posteriores de estado y las probabilidades conjuntas de estado
print("Probabilidades posteriores de estado:")
print(gamma)
print("Probabilidades conjuntas de estado:")
print(xi)

