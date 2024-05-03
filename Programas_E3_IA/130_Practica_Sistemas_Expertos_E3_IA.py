# Practica_130_Sistemas_Expertos_E3_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Sistemas_Expertos

from pyknow import *

# Definimos una clase para nuestro sistema experto que hereda de `KnowledgeEngine`
class DiagnosticoGripe(KnowledgeEngine):
    @Rule()
    def pregunta_sintomas(self):
        # Pedimos al usuario ingresar los síntomas
        fiebre = input("¿Tiene fiebre? (sí/no): ").lower()
        tos = input("¿Tiene tos? (sí/no): ").lower()
        dolor_garganta = input("¿Tiene dolor de garganta? (sí/no): ").lower()
        
        # Llamamos a la regla de inferencia con los síntomas ingresados
        self.declare(Fact(fiebre=fiebre, tos=tos, dolor_garganta=dolor_garganta))

    @Rule(AND(Fact(fiebre="sí"), Fact(tos="sí"), Fact(dolor_garganta="sí")))
    def diagnostico_gripe(self):
        # Si el paciente tiene fiebre, tos y dolor de garganta, se diagnostica gripe
        print("Usted podría tener gripe.")
    
    @Rule(OR(Fact(fiebre="no"), Fact(tos="no"), Fact(dolor_garganta="no")))
    def no_diagnostico_gripe(self):
        # Si el paciente no tiene alguno de estos síntomas, es poco probable que tenga gripe
        print("Es poco probable que tenga gripe.")

# Creamos una instancia de nuestro sistema experto
sistema_experto = DiagnosticoGripe()

# Ejecutamos el sistema experto
sistema_experto.reset()
sistema_experto.run()

