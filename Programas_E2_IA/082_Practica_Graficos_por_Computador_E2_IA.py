# Practica_082_Graficos_por_Computador_E2_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Graficos_por_Computador

import random

def lanzamiento_dado(n):

    resultados = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}  # Inicializamos un diccionario para contar los resultados
    
    for _ in range(n):  # Repetimos el lanzamiento del dado n veces
        resultado = random.randint(1, 6)  # Generamos un número aleatorio entre 1 y 6 (inclusive)
        resultados[resultado] += 1  # Incrementamos el contador para el resultado obtenido
    
    probabilidades = {key: value / n for key, value in resultados.items()}  # Calculamos las probabilidades
    
    return probabilidades

# Simulamos el lanzamiento del dado 10000 veces
lanzamientos = 10000
probabilidades = lanzamiento_dado(lanzamientos)

# Imprimimos los resultados
for resultado, probabilidad in probabilidades.items():
    print(f"Resultado: {resultado}, Probabilidad: {probabilidad}")

# Verificamos que la suma de las probabilidades sea aproximadamente 1
suma_probabilidades = sum(probabilidades.values())
print(f"Suma de probabilidades: {suma_probabilidades}")

