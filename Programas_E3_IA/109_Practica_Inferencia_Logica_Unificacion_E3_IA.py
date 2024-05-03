# Practica_109_Inferencia_Logica_Unificacion_E3_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Inferencia_Logica_Unificacion

def unify_var(var, x, theta): # Unifica una variable con una expresión, almacenando la sustitución en theta

    if var in theta:
        return unify(theta[var], x, theta)
    elif x in theta:
        return unify(var, theta[x], theta)
    else:
        theta[var] = x
        return theta


def unify(x, y, theta): # Algoritmo de unificación para dos expresiones

    if theta is None:
        return None
    elif x == y:
        return theta
    elif isinstance(x, str) and x.islower():
        return unify_var(x, y, theta)
    elif isinstance(y, str) and y.islower():
        return unify_var(y, x, theta)
    elif isinstance(x, list) and isinstance(y, list):
        if len(x) != len(y):
            return None
        for i in range(len(x)):
            theta = unify(x[i], y[i], theta)
            if theta is None:
                return None
        return theta
    else:
        return None

if __name__ == "__main__":
    # Definimos las expresiones a unificar
    expression1 = ['P', 'x', 'f', 'x', 'g', 'y']
    expression2 = ['P', 'A', 'f', 'z', 'g', 'A']

    # Inicializamos el conjunto de sustituciones vacío
    theta = {}

    # Realizamos la unificación
    result = unify(expression1, expression2, theta)

    # Imprimimos el resultado
    print("Conjunto de sustituciones:", result)
