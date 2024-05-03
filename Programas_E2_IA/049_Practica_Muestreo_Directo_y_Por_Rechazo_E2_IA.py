# Practica_049_Muestreo_Directo_y_Por_Rechazo_E2_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria en Mecatronica

# Programa_Muestreo_Directo_y_Por_Rechazo

import random

def muestreo_directo(distribucion):
    # Generar un número aleatorio entre 0 y 1
    aleatorio = random.random()
    
    # Inicializar la suma acumulada de probabilidades
    suma_acumulada = 0
    
    # Iterar sobre los valores y sus probabilidades en la distribución
    for valor, probabilidad in distribucion.items():
        # Acumular la probabilidad del valor actual
        suma_acumulada += probabilidad
        
        # Si la suma acumulada supera el número aleatorio, devolver el valor
        if suma_acumulada >= aleatorio:
            return valor

# Ejemplo de una distribución de probabilidad discreta
distribucion = {'A': 0.2, 'B': 0.3, 'C': 0.5}

# Generar una muestra utilizando el método de muestreo directo
muestra = muestreo_directo(distribucion)

# Imprimir la muestra generada
print("Muestra generada mediante muestreo directo:", muestra)
