# Practica_139_Vigilancia_de_Ejecucion_y_Replanificacion_E3_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Vigilancia_de_Ejecucion_y_Replanificacion

# Definimos una función para ejecutar el plan inicial
def ejecutar_plan(plan):
    print("Ejecutando plan inicial:")
    for accion in plan:
        print("Ejecutando:", accion)

# Definimos el plan inicial
plan_inicial = ['accion1', 'accion2', 'accion3']

# Ejecutamos el plan inicial
ejecutar_plan(plan_inicial)

# Supongamos que durante la ejecución del plan inicial se detecta un problema y necesitamos replanificar
# Por simplicidad, simplemente agregaremos una acción adicional al plan replanificado

# Replanificamos el plan en función del problema detectado
print("\nReplanificando el plan debido a un problema detectado:")
plan_replanificado = plan_inicial + ['accion_extra']

# Ejecutamos el plan replanificado
ejecutar_plan(plan_replanificado)
