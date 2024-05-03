# Practica_120_Conjuntos_Difusos_E3_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Conjuntos_Difusos

# Definición de la función de pertenencia triangular 
def triangular(x, a, b, c):

    if x <= a or x >= c:
        return 0  # Si x está fuera del rango, su grado de pertenencia es cero
    elif a < x <= b:
        return (x - a) / (b - a)  # Pendiente positiva
    else:
        return (c - x) / (c - b)  # Pendiente negativa

if __name__ == "__main__":
    # Definimos los parámetros del conjunto difuso triangular
    a = 10  # Punto de inicio de la función de pertenencia
    b = 20  # Punto medio de la función de pertenencia (valor máximo)
    c = 30  # Punto final de la función de pertenencia
    
    # Valor para el que se calculará el grado de pertenencia
    x = 15

    # Calculamos el grado de pertenencia utilizando la función triangular
    pertenencia = triangular(x, a, b, c)

    # Imprimimos el grado de pertenencia
    print(f"El valor {x} tiene un grado de pertenencia de {pertenencia} al conjunto difuso triangular definido por ({a}, {b}, {c})")

