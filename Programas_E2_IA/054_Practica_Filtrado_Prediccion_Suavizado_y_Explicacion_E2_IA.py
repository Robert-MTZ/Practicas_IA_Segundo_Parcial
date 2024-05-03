# Practica_054_Filtrado_Prediccion_Suavizado_y_Explicacion_E2_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria en Mecatronica

# Programa_Filtrado_Prediccion_Suavizado_y_Explicacion

import numpy as np # Genera numeros aleatorios y realizar calculos matriciales de manera eficiente

class FiltroKalman:
    def __init__(self, A, B, H, Q, R, x0, P0):
      
        self.A = A
        self.B = B
        self.H = H
        self.Q = Q
        self.R = R
        self.x = x0
        self.P = P0
    
    def paso_prediccion(self, u=None):
    
        # Predicción del estado
        x_pred = np.dot(self.A, self.x)
        if u is not None:
            x_pred += np.dot(self.B, u)
        
        # Predicción de la covarianza del estado
        P_pred = np.dot(np.dot(self.A, self.P), self.A.T) + self.Q
        
        return x_pred, P_pred
    
    def paso_actualizacion(self, z):
     
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
A = np.array([[1, 1],
              [0, 1]])
B = np.zeros((2, 1))
H = np.array([[1, 0]])
Q = np.eye(2) * 0.01
R = np.eye(1) * 1
x0 = np.array([[0],
               [0]])
P0 = np.eye(2) * 0.1

# Creamos una instancia del filtro de Kalman
filtro = FiltroKalman(A, B, H, Q, R, x0, P0)

# Generamos datos simulados
np.random.seed(0)
datos_simulados = [np.random.normal(loc=i, scale=1) for i in range(10)]

# Ejecutamos el filtro de Kalman
estados_filtrados = []
for z in datos_simulados:
    x_pred, P_pred = filtro.paso_prediccion()
    x_filt, P_filt = filtro.paso_actualizacion(z)
    estados_filtrados.append(x_filt[0, 0])

# Imprimimos los estados filtrados
print("Estados filtrados:", estados_filtrados)
