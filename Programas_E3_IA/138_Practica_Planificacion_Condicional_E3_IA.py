# Practica_138_Planificacion_Condicional_E3_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Planificacion_Condicional

# Definimos el problema de planificación como una lista de tuplas (accion, precondiciones, efectos)
problema_planificacion = [
    ('accion1', ['condicion1'], ['efecto1']),
    ('accion2', ['condicion2'], ['efecto2']),
    ('accion3', ['condicion1', 'condicion2'], ['efecto3'])
]

# Función para planificar acciones bajo ciertas condiciones
def planificar_acciones(problema, condiciones):
    acciones_planificadas = []

    # Iteramos sobre cada acción en el problema de planificación
    for accion, precondiciones, efectos in problema:
        # Verificamos si todas las precondiciones de la acción están presentes en las condiciones
        if all(precondicion in condiciones for precondicion in precondiciones):
            # Si se cumplen todas las precondiciones, añadimos la acción a las acciones planificadas
            acciones_planificadas.append(accion)

    return acciones_planificadas

# Definimos las condiciones bajo las cuales queremos planificar las acciones
condiciones_actuales = ['condicion1']

# Planificamos las acciones bajo las condiciones actuales
acciones_planificadas = planificar_acciones(problema_planificacion, condiciones_actuales)

# Imprimimos las acciones planificadas
print("Acciones planificadas bajo las condiciones actuales:", acciones_planificadas)

