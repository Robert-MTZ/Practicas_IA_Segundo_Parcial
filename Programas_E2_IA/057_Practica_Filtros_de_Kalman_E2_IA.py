# Practica_057_Filtros_de_Kalman_E2_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria en Mecatronica

# Programa_Filtros_de_Kalman

import numpy as np # Genera numeros aleatorios y realizar calculos matriciales de manera eficiente

class FiltroKalman:
    def __init__(self, A, B, H, Q, R, x0, P0):
    
        self.A = np.array(A)  # Matriz de transición de estado
        self.B = np.array(B) if B is not None else None  # Matriz de control
        self.H = np.array(H)  # Matriz de observación
        self.Q = np.array(Q)  # Matriz de covarianza del ruido de proceso
        self.R = np.array(R)  # Matriz de covarianza del ruido de medición
        self.x = np.array(x0)  # Estado inicial estimado
        self.P = np.array(P0)  # Matriz de covarianza inicial del estado estimado
        self.dim_estado = len(x0)  # Dimensión del estado
    
    def predecir(self, u=None):
        
        # Predicción del estado
        x_pred = np.dot(self.A, self.x)
        if self.B is not None and u is not None:
            x_pred += np.dot(self.B, u)
        
        # Predicción de la covarianza del estado
        P_pred = np.dot(np.dot(self.A, self.P), self.A.T) + self.Q
        
        return x_pred, P_pred
    
    def actualizar(self, z):
      
        # Innovación
        innovacion = z - np.dot(self.H, self.x)
        
        # Covarianza de la innovación
        S = np.dot(np.dot(self.H, self.P), self.H.T) + self.R
        
        # Ganancia de Kalman
        K = np.dot(np.dot(self.P, self.H.T), np.linalg.inv(S))
        
        # Actualización del estado
        x_nuevo = self.x + np.dot(K, innovacion)
        
        # Actualización de la covarianza del estado
        P_nuevo = self.P - np.dot(np.dot(K, self.H), self.P)
        
        return x_nuevo, P_nuevo

# Parámetros del modelo del filtro de Kalman
A = [[1, 1],
     [0, 1]]  # Matriz de transición de estado
B = None  # Matriz de control (en este caso no se utiliza)
H = [[1, 0]]  # Matriz de observación
Q = [[0.01, 0],
     [0, 0.01]]  # Matriz de covarianza del ruido de proceso
R = [[1]]  # Matriz de covarianza del ruido de medición
x0 = [[0],
      [0]]  # Estado inicial estimado
P0 = [[0.1, 0],
      [0, 0.1]]  # Matriz de covarianza inicial del estado estimado

# Creamos una instancia del filtro de Kalman
filtro = FiltroKalman(A, B, H, Q, R, x0, P0)

# Generamos una secuencia de observaciones
observaciones = np.array([[i] for i in range(10)])

# Ejecutamos el filtro de Kalman
estados_estimados = []
for z in observaciones:
    x_pred, P_pred = filtro.predecir()
    x_filt, P_filt = filtro.actualizar(z)
    estados_estimados.append(x_filt[0, 0])

# Imprimimos los estados estimados
print("Estados estimados:", estados_estimados)
