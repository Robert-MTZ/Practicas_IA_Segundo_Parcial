# Practica_129_Incertidumbre_y_Factores_de_Certeza_E3_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Incertidumbre_y_Factores_de_Certeza

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Definimos las variables de entrada y salida
calidad = ctrl.Antecedent(np.arange(0, 11, 1), 'calidad')
servicio = ctrl.Antecedent(np.arange(0, 11, 1), 'servicio')
propina = ctrl.Consequent(np.arange(0, 26, 1), 'propina')

# Definimos las funciones de membresía para las variables de entrada y salida
calidad['mala'] = fuzz.trimf(calidad.universe, [0, 0, 5])
calidad['buena'] = fuzz.trimf(calidad.universe, [0, 5, 10])
servicio['malo'] = fuzz.trimf(servicio.universe, [0, 0, 5])
servicio['bueno'] = fuzz.trimf(servicio.universe, [0, 5, 10])
propina['baja'] = fuzz.trimf(propina.universe, [0, 0, 13])
propina['media'] = fuzz.trimf(propina.universe, [0, 13, 25])

# Visualizamos las funciones de membresía
calidad.view()
servicio.view()
propina.view()

# Definimos las reglas
regla1 = ctrl.Rule(calidad['mala'] | servicio['malo'], propina['baja'])
regla2 = ctrl.Rule(servicio['bueno'], propina['media'])
regla3 = ctrl.Rule(calidad['buena'] & servicio['bueno'], propina['media'])

# Creamos el sistema de control
sistema_control = ctrl.ControlSystem([regla1, regla2, regla3])
sistema = ctrl.ControlSystemSimulation(sistema_control)

# Simulamos el sistema de control
sistema.input['calidad'] = 6.5
sistema.input['servicio'] = 9.8
sistema.compute()

# Imprimimos el resultado
print("Propina:", sistema.output['propina'])
propina.view(sim=sistema)

