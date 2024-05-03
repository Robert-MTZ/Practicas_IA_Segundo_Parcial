# Practica_122_Fuzzy_CLIPS_E3_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Fuzzy_CLIPS

import clips

# Creamos una nueva instancia del entorno CLIPS
env = clips.Environment()

# Cargamos el módulo Fuzzy CLIPS
env.load("clips/fuzzy.clp")

# Definimos las reglas difusas
env.build("(fuzzy-or (very-low (<= ?x 20)) (low (<= ?x 40)) (medium (<= ?x 60)) (high (<= ?x 80)) (very-high (<= ?x 100)))")

# Definimos una regla difusa de ejemplo
env.build("(defrule example-rule (temperature ?t) => (assert (speed (fuzzy-value ?t very-low))))")

# Insertamos un hecho con la temperatura
env.assert_string("(temperature 30)")

# Ejecutamos el sistema
env.run()

# Imprimimos los resultados
for fact in env.facts():
    print(fact)

# Cerramos el entorno CLIPS
env.clear()

