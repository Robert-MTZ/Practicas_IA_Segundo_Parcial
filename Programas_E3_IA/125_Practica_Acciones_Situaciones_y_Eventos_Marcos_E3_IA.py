# Practica_125_Acciones_Situaciones_y_Eventos_Marcos_E3_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Acciones_Situaciones_y_Eventos_Marcos

# Definimos una clase para representar un marco de situación o evento
class Marco:
    def __init__(self, nombre, ubicacion, personas):
        self.nombre = nombre  # Nombre del marco
        self.ubicacion = ubicacion  # Ubicación asociada al marco
        self.personas = personas  # Lista de personas presentes en el marco

# Creamos instancias de la clase Marco para representar diferentes situaciones o eventos
situacion_1 = Marco("Fiesta de cumpleaños", "Casa de Juan", ["Juan", "María", "Pedro"])
situacion_2 = Marco("Reunión de trabajo", "Oficina", ["Ana", "Carlos", "Laura"])

# Imprimimos la información de cada marco
print("Situación 1:")
print("Nombre:", situacion_1.nombre)
print("Ubicación:", situacion_1.ubicacion)
print("Personas:", situacion_1.personas)
print()

print("Situación 2:")
print("Nombre:", situacion_2.nombre)
print("Ubicación:", situacion_2.ubicacion)
print("Personas:", situacion_2.personas)

