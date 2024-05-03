# Practica_141_Tipos_de_Razonamiento_y_Aprendizaje_E3_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Tipos_de_Razonamiento_y_Aprendizaje

from pyknow import *

# Definimos una clase para nuestro motor de reglas
class SistemaRecomendacion(KnowledgeEngine):
    @DefFacts()
    def cargar_datos(self):
        # Definimos los datos de entrada (hechos iniciales)
        yield Fact(tiempo="soleado")
        yield Fact(temperatura="calida")
        yield Fact(humedad="alta")

    # Definimos las reglas de recomendación
    @Rule(AND(Fact(tiempo="soleado"),
              Fact(temperatura="calida"),
              Fact(humedad="alta")))
    def recomendar_actividad(self):
        print("Condiciones actuales: soleado, temperatura cálida, humedad alta.")
        print("Te recomiendo ir a la playa.")

    @Rule(AND(Fact(tiempo="nublado"),
              Fact(temperatura="templada"),
              Fact(humedad="alta")))
    def recomendar_actividad2(self):
        print("Condiciones actuales: nublado, temperatura templada, humedad alta.")
        print("Te recomiendo ir a hacer senderismo.")

    @Rule(AND(Fact(tiempo="lluvioso"),
              Fact(temperatura="fria"),
              Fact(humedad="alta")))
    def recomendar_actividad3(self):
        print("Condiciones actuales: lluvioso, temperatura fría, humedad alta.")
        print("Te recomiendo quedarte en casa y ver una película.")

    # Regla por defecto si ninguna de las reglas anteriores se cumple
    @Rule()
    def recomendar_actividad_default(self):
        print("No se pueden hacer recomendaciones para las condiciones actuales.")


# Creamos una instancia del motor de reglas
sistema = SistemaRecomendacion()

# Ejecutamos el motor de reglas
sistema.reset()
sistema.run()

