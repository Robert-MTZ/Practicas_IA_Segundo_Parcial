# Practica_121_Inferencia_Difusa_E3_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Inferencia_Difusa

# Importar las librerías necesarias
import numpy as np

# Definir las funciones de membresía para la temperatura y la humedad
def membresia_temperatura(x):
    if x <= 20:
        return 1
    elif 20 < x <= 25:
        return (25 - x) / 5
    else:
        return 0

def membresia_humedad(x):
    if x <= 50:
        return 1
    elif 50 < x <= 60:
        return (60 - x) / 10
    else:
        return 0

# Definir las reglas difusas
def reglas_difusas(temperatura, humedad):
    # Reglas difusas para la velocidad del ventilador
    if temperatura == "baja" and humedad == "baja":
        return "baja"
    elif temperatura == "media" or humedad == "media":
        return "media"
    else:
        return "alta"

# Definir la función de inferencia difusa
def inferencia_difusa(temperatura, humedad):
    # Calcular el grado de membresía para la temperatura y la humedad
    memb_temperatura = membresia_temperatura(temperatura)
    memb_humedad = membresia_humedad(humedad)
    
    # Aplicar las reglas difusas
    velocidad = reglas_difusas(temperatura, humedad)
    
    # Retornar la velocidad difusa resultante
    return velocidad

if __name__ == "__main__":
    # Temperatura y humedad de entrada
    temperatura = 22
    humedad = 55
    
    # Realizar inferencia difusa para obtener la velocidad del ventilador
    velocidad = inferencia_difusa(temperatura, humedad)
    
    # Imprimir la velocidad resultante
    print("La velocidad del ventilador es:", velocidad)
