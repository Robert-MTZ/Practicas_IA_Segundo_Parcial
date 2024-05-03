# Practica_128_Razonamiento_por_Defecto_y_No_Monotonico_E3_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Razonamiento_por_Defecto_y_No_Monotonico

from pyknow import *

# Definimos un hecho inicial sobre la relación entre aves y volar
@DefFacts()
def inicial_facts():
    yield Fact(aves_pueden_volar=True)

# Definimos una regla de producción para inferir si un animal puede volar
class AnimalPuedeVolar(Rule):
    salience = 1  # Prioridad de la regla

    @Rule(Fact(ave=P(True)))
    def aves_pueden_volar(self):
        print("El animal puede volar")

    @Rule(Fact(ave=P(False)))
    def aves_no_pueden_volar(self):
        print("El animal no puede volar")

# Creamos un motor de inferencia y cargamos las reglas definidas
engine = KnowledgeEngine()
engine.reset()
engine.declare(Fact(ave=True))

# Ejecutamos el motor de inferencia
engine.run()

