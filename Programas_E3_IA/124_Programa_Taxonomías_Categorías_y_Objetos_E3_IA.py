# Practica_124_Taxonomías_Categorías_y_Objetos_E3_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Taxonomías_Categorías_y_Objetos

# Creamos la estructura de taxonomía utilizando diccionarios anidados
taxonomia = {
    "animales": {
        "mamiferos": ["perro", "gato", "elefante"],
        "aves": ["pajaro", "aguila", "pato"]
    },
    "frutas": ["manzana", "banana", "naranja"],
    "vehiculos": {
        "terrestres": ["coche", "moto", "bicicleta"],
        "aereos": ["avion", "helicoptero"],
        "maritimos": ["barco", "submarino"]
    }
}

# Función para imprimir la taxonomía
def imprimir_taxonomia(taxonomia, nivel=0):
    for clave, valor in taxonomia.items():
        if isinstance(valor, dict):  # Si el valor es un diccionario, es una categoría
            print("\t" * nivel + clave.capitalize() + ":")
            imprimir_taxonomia(valor, nivel + 1)  # Llamada recursiva para imprimir las subcategorías
        else:  # Si el valor es una lista, son objetos
            print("\t" * nivel + clave.capitalize() + ": " + ", ".join(valor))

# Imprimimos la taxonomía
print("Taxonomía:")
imprimir_taxonomia(taxonomia)

