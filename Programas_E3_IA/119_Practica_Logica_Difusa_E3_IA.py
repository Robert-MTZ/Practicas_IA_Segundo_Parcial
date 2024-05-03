# Practica_119_Logica_Difusa_E3_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Logica_Difusa

# Importar las librerías necesarias
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Crear las variables de entrada y salida difusas
temperatura = ctrl.Antecedent(np.arange(0, 101, 1), 'temperatura')
velocidad = ctrl.Consequent(np.arange(0, 101, 1), 'velocidad')

# Definir las funciones de membresía para la temperatura
temperatura['fría'] = fuzz.trimf(temperatura.universe, [0, 0, 50])
temperatura['normal'] = fuzz.trimf(temperatura.universe, [0, 50, 100])
temperatura['caliente'] = fuzz.trimf(temperatura.universe, [50, 100, 100])

# Definir las funciones de membresía para la velocidad
velocidad['baja'] = fuzz.trimf(velocidad.universe, [0, 0, 50])
velocidad['media'] = fuzz.trimf(velocidad.universe, [0, 50, 100])
velocidad['alta'] = fuzz.trimf(velocidad.universe, [50, 100, 100])

# Definir las reglas difusas
regla1 = ctrl.Rule(temperatura['fría'], velocidad['baja'])
regla2 = ctrl.Rule(temperatura['normal'], velocidad['media'])
regla3 = ctrl.Rule(temperatura['caliente'], velocidad['alta'])

# Crear el sistema de control difuso
sistema_ctrl = ctrl.ControlSystem([regla1, regla2, regla3])
sistema = ctrl.ControlSystemSimulation(sistema_ctrl)

# Entrada de temperatura
sistema.input['temperatura'] = 70

# Calcular el resultado
sistema.compute()

# Imprimir la velocidad resultante
print("Velocidad del ventilador:", sistema.output['velocidad'])

# Visualizar las funciones de membresía y las reglas
temperatura.view()
velocidad.view()

