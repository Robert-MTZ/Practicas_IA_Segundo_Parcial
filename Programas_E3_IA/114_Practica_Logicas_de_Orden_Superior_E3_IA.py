# Practica_114_Logicas_de_Orden_Superior_E3_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Programacion_Logicas_de_Orden_Superior

from functools import reduce  # Importamos reduce desde functools

# Definimos una lista de números
numbers = [1, 2, 3, 4, 5]

# Función de orden superior: map
# Aplicamos la función lambda que duplica cada número a la lista numbers
mapped_numbers = list(map(lambda x: x * 2, numbers))

# Función de orden superior: filter
# Filtramos los números pares de la lista numbers
filtered_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Función de orden superior: reduce
# Sumamos todos los números de la lista numbers utilizando reduce
sum_of_numbers = reduce(lambda x, y: x + y, numbers)

# Imprimimos los resultados
print("Lista original:", numbers)
print("Lista después de aplicar map (duplicar cada número):", mapped_numbers)
print("Lista después de aplicar filter (números pares):", filtered_numbers)
print("Suma de todos los números:", sum_of_numbers)
