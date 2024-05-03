# Practica_041_Distribucion_de_Probabilidad_E2_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria en Mecatronica

# Programa_Distribucion_de_Probabilidad

import numpy as np # Genera numeros aleatorios y realizar calculos matriciales de manera eficiente
import matplotlib.pyplot as plt #  Visualizar datos en Python

def distribucion_de_probabilidad(datos):
    # Calculamos el número total de datos
    total_datos = len(datos)
    
    # Creamos un diccionario para almacenar la frecuencia de cada valor
    frecuencia = {}
    
    # Calculamos la frecuencia de cada valor en los datos
    for valor in datos:
        if valor in frecuencia:
            frecuencia[valor] += 1
        else:
            frecuencia[valor] = 1
    
    # Calculamos la probabilidad de cada valor dividiendo su frecuencia por el total de datos
    distribucion_probabilidad = {valor: frecuencia[valor] / total_datos for valor in frecuencia}
    
    return distribucion_probabilidad

# Generamos un conjunto de datos aleatorios
datos = np.random.randint(1, 11, size=100)

# Calculamos la distribución de probabilidad
distribucion = distribucion_de_probabilidad(datos)

# Imprimimos la distribución de probabilidad
print("Distribución de Probabilidad:")
for valor, probabilidad in distribucion.items():
    print(f"Valor: {valor}, Probabilidad: {probabilidad:.4f}")

# Extraemos los valores y las probabilidades del diccionario de distribución
valores = list(distribucion.keys())
probabilidades = list(distribucion.values())

# Creamos un gráfico de barras para visualizar la distribución de probabilidad
plt.bar(valores, probabilidades)
plt.xlabel('Valores')
plt.ylabel('Probabilidad')
plt.title('Distribución de Probabilidad')
plt.show()
    
