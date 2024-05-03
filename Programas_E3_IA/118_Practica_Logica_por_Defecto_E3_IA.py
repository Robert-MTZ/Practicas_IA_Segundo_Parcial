# Practica_118_Logica_por_Defecto_E3_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Logica_por_Defecto

# Importar la librería random para generar números aleatorios
import random

# Definir una clase para representar una hipótesis (en este caso, un diagnóstico)
class Hipotesis:
    def __init__(self, nombre, probabilidad):
        self.nombre = nombre
        self.probabilidad = probabilidad

# Función para actualizar las probabilidades de las hipótesis según la evidencia
def actualizar_probabilidades(hipotesis, evidencia):
    total_probabilidad_evidencia = sum(evidencia.values())
    for h in hipotesis:
        h.probabilidad *= evidencia[h.nombre] / total_probabilidad_evidencia

# Función para imprimir las probabilidades de las hipótesis
def imprimir_probabilidades(hipotesis):
    print("Probabilidades de las hipótesis:")
    for h in hipotesis:
        print(f"{h.nombre}: {h.probabilidad:.2f}")

# Definir las hipótesis iniciales y sus probabilidades por defecto
hipotesis = [
    Hipotesis("Enfermedad A", 0.1),  # Probabilidad por defecto de tener la Enfermedad A
    Hipotesis("Enfermedad B", 0.2),  # Probabilidad por defecto de tener la Enfermedad B
    Hipotesis("Enfermedad C", 0.3)   # Probabilidad por defecto de tener la Enfermedad C
]

# Definir la evidencia (resultados de pruebas médicas) y sus probabilidades condicionales
evidencia = {
    "Enfermedad A": 0.9,  # Probabilidad de que las pruebas confirmen la Enfermedad A
    "Enfermedad B": 0.8,  # Probabilidad de que las pruebas confirmen la Enfermedad B
    "Enfermedad C": 0.7   # Probabilidad de que las pruebas confirmen la Enfermedad C
}

# Imprimir las probabilidades iniciales de las hipótesis
imprimir_probabilidades(hipotesis)

# Actualizar las probabilidades de las hipótesis según la evidencia
actualizar_probabilidades(hipotesis, evidencia)

# Imprimir las probabilidades actualizadas de las hipótesis
imprimir_probabilidades(hipotesis)
