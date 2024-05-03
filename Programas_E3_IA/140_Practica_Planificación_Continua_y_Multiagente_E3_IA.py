# Practica_140_Planificación_Continua_y_Multiagente_E3_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Planificación_Continua_y_Multiagente

import time

# Definimos la clase Agente
class Agente:
    def __init__(self, nombre):
        self.nombre = nombre

    # Método para realizar una acción
    def realizar_accion(self, accion):
        print(f"{self.nombre} realiza la acción: {accion}")
        time.sleep(1)  # Simulamos la ejecución de la acción

# Definimos la función principal del programa
def main():
    # Creamos dos agentes
    agente1 = Agente("Agente 1")
    agente2 = Agente("Agente 2")

    # Definimos la meta
    meta = "Lograr la meta"

    # Iniciamos el ciclo de planificación continua
    while True:
        # Los agentes colaboran para lograr la meta
        agente1.realizar_accion("Acción 1")
        agente2.realizar_accion("Acción 2")
        
        # Verificamos si la meta ha sido alcanzada
        if meta_alcanzada():
            print("¡Meta alcanzada!")
            break

        # Simulamos el cambio de condiciones o de la meta
        cambiar_condiciones()

        # Esperamos un tiempo antes de la siguiente iteración
        time.sleep(2)

# Función para verificar si la meta ha sido alcanzada (simulada)
def meta_alcanzada():
    # En este ejemplo simple, la meta se alcanza aleatoriamente
    import random
    return random.choice([True, False])

# Función para simular cambios en las condiciones o la meta
def cambiar_condiciones():
    print("Cambiando condiciones...")
    # Aquí se simularían cambios en el entorno o en las metas

# Llamamos a la función principal del programa
if __name__ == "__main__":
    main()

