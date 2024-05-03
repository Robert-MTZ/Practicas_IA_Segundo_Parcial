# Practica_101_Equivalencia_Validez_y_Satisfacibilidad_E3_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Equivalencia_Validez_y_Satisfacibilidad


from sympy import symbols, Not, And, Or, Implies, Equivalent, satisfiable, simplify_logic

def is_equivalent(expr1, expr2):

    return Equivalent(expr1, expr2)

def is_valid(expr):

    return expr.is_valid()

def is_satisfiable(expr):

    return satisfiable(expr)


if __name__ == "__main__":
    # Definimos algunas variables simbólicas
    p, q, r = symbols('p q r')

    # Expresiones lógicas para probar
    expr1 = And(p, q)
    expr2 = Or(Not(p), Not(q))
    expr3 = Implies(p, q)

    # Verificamos la equivalencia entre expr1 y expr2
    print("¿expr1 es equivalente a expr2?", is_equivalent(expr1, expr2))

    # Verificamos si expr3 es válida
    print("¿expr3 es válida?", is_valid(expr3))

    # Verificamos si expr1 es satisfacible
    print("¿expr1 es satisfacible?", is_satisfiable(expr1))

