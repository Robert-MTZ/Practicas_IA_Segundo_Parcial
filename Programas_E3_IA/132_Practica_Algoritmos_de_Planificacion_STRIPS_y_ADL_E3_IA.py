# Practica_132_Algoritmos_de_Planificacion_STRIPS_y_ADL_E3_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Algoritmos_de_Planificacion_STRIPS_y_ADL

import pyhop

# Definimos el estado inicial del problema
estado_inicial = {
    'en_mesa': ['A', 'C'],   # bloques en la mesa
    'sobre': [('B', 'A'), ('D', 'C')],  # bloques apilados: (bloque_superior, bloque_inferior)
    'mano_vacia': True  # mano vacía al principio
}

# Definimos el objetivo del problema
objetivo = {
    'sobre': [('B', 'C'), ('A', 'D')]  # queremos apilar B sobre C y A sobre D
}

# Definimos las acciones posibles para el agente
def mover_agarrar(estado, bloque):
    if estado['mano_vacia'] and bloque in estado['en_mesa']:
        nuevo_estado = estado.copy()
        nuevo_estado['mano_vacia'] = False
        nuevo_estado['en_mesa'].remove(bloque)
        return nuevo_estado, [('agarrar', bloque)]
    else:
        return False

def mover_soltar(estado, bloque):
    if not estado['mano_vacia']:
        nuevo_estado = estado.copy()
        nuevo_estado['mano_vacia'] = True
        nuevo_estado['en_mesa'].append(bloque)
        return nuevo_estado, [('soltar', bloque)]
    else:
        return False

def mover_apilar(estado, bloque1, bloque2):
    if bloque1 != bloque2 and (bloque1, bloque2) in estado['sobre']:
        nuevo_estado = estado.copy()
        nuevo_estado['sobre'].remove((bloque1, bloque2))
        nuevo_estado['sobre'].append((bloque1, bloque2))
        return nuevo_estado, [('apilar', bloque1, bloque2)]
    else:
        return False

# Añadimos las acciones al planificador
pyhop.declare_operators(mover_agarrar, mover_soltar, mover_apilar)

# Definimos los métodos posibles para resolver el objetivo
def mover_apilar_todos(estado, objetivo):
    movimientos = []
    for b1, b2 in objetivo['sobre']:
        if (b1, b2) not in estado['sobre']:
            movimientos.append(('apilar', b1, b2))
    return movimientos

# Añadimos el método al planificador
pyhop.declare_methods('mover_todos', mover_apilar_todos)

# Resolvemos el problema
plan = pyhop.pyhop(estado_inicial, [('mover_todos', objetivo)], verbose=3)

# Imprimimos el plan encontrado
print("Plan encontrado:")
for accion in plan:
    print(accion)

