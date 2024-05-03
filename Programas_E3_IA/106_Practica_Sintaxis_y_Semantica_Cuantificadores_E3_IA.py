# Practica_106_Sintaxis_y_Semantica_Cuantificadores_E3_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Sintaxis_y_Semantica_Cuantificadores

from sympy import symbols, forall

def check_universal_quantifier(predicate, domain): #  Verifica si una afirmación cuantificada universalmente es verdadera para un dominio dado

    for element in domain:
        if not predicate.subs({x: element}):
            return False
    return True

# Definimos las variables simbólicas
x = symbols('x')

# Por ejemplo, queremos verificar si para todo x en el dominio de los enteros, x + 1 es mayor que x
universal_statement = forall(x, x + 1 > x)

# Definimos el dominio de los enteros
integer_domain = range(-10, 11)  # Seleccionamos un rango de -10 a 10 como dominio

# Verificamos si la afirmación es verdadera para el dominio de los enteros
result = check_universal_quantifier(universal_statement, integer_domain)

# Imprimimos el resultado
print("¿La afirmación es verdadera para todo x en el dominio de los enteros?", result)

