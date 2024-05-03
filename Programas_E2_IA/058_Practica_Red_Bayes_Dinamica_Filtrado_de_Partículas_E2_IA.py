# Practica_058_Red_Bayes_Dinamica_Filtrado_de_Partículas_E2_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria en Mecatronica

# Programa_Red_Bayes_Dinamica_Filtrado_de_Partículas

import numpy as np # Genera numeros aleatorios y realizar calculos matriciales de manera eficiente

class Particula:
    def __init__(self, valor, peso):
     
        self.valor = valor
        self.peso = peso

class FiltradoParticulas:
    def __init__(self, modelo_transicion, modelo_emision, num_particulas):
       
        self.modelo_transicion = modelo_transicion
        self.modelo_emision = modelo_emision
        self.num_particulas = num_particulas
        self.particulas = []
    
    def inicializar_particulas(self, estado_inicial):
      
        for _ in range(self.num_particulas):
            self.particulas.append(Particula(estado_inicial, 1.0 / self.num_particulas))
    
    def predecir(self):
      
        for particula in self.particulas:
            # Modelo de transición: generamos una nueva muestra del estado de la partícula
            particula.valor = self.modelo_transicion(particula.valor)
    
    def actualizar(self, observacion):
    
        # Calculamos los pesos de las partículas en base a la verosimilitud de la observación
        for particula in self.particulas:
            verosimilitud = self.modelo_emision(observacion, particula.valor)
            particula.peso *= verosimilitud
        
        # Normalizamos los pesos para que sumen 1
        total_pesos = sum(particula.peso for particula in self.particulas)
        for particula in self.particulas:
            particula.peso /= total_pesos
    
    def resample(self):
    
        # Creamos una lista de índices para el re-muestreo utilizando el método de la ruleta
        pesos_acumulados = np.cumsum([particula.peso for particula in self.particulas])
        nuevos_indices = np.searchsorted(pesos_acumulados, np.random.rand(self.num_particulas))
        
        # Creamos una nueva lista de partículas re-muestreadas
        nuevas_particulas = []
        for indice in nuevos_indices:
            nuevas_particulas.append(Particula(self.particulas[indice].valor, 1.0 / self.num_particulas))
        
        # Reemplazamos las partículas antiguas por las nuevas
        self.particulas = nuevas_particulas
    
    def estimar_estado(self):
       
        # Estimamos el estado como una media ponderada de los estados de las partículas
        estado_estimado = np.mean([particula.valor for particula in self.particulas], axis=0)
        return estado_estimado

# Modelos de transición y emisión
def modelo_transicion(estado):

    return estado + np.random.normal(0, 0.1, size=estado.shape)

def modelo_emision(observacion, estado):
   
    return np.exp(-0.5 * np.sum((observacion - estado) ** 2))

# Creamos una instancia del filtrado de partículas
filtro_particulas = FiltradoParticulas(modelo_transicion, modelo_emision, num_particulas=100)

# Inicializamos las partículas con un estado inicial
estado_inicial = np.array([0])
filtro_particulas.inicializar_particulas(estado_inicial)

# Simulamos la evolución del sistema y las observaciones
observaciones_simuladas = []
for _ in range(50):
    filtro_particulas.predecir()
    estado_real = modelo_transicion(estado_inicial)
    observacion_simulada = modelo_emision(estado_real, estado_real)
    filtro_particulas.actualizar(observacion_simulada)
    filtro_particulas.resample()
    estado_estimado = filtro_particulas.estimar_estado()
    observaciones_simuladas.append(observacion_simulada)

# Imprimimos las observaciones simuladas
print("Observaciones simuladas:", observaciones_simuladas)

