# Practica_127_Reglas_Redes_Semanticas_y_Logica_Descriptiva_E3_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Reglas_Redes_Semanticas_y_Logica_Descriptiva

# Definimos un conjunto de reglas para inferir el color de un objeto
reglas = {
    ("forma", "redondo"): "rojo",
    ("forma", "cuadrado"): "azul",
    ("forma", "triangular"): "verde",
    ("tamaño", "pequeño"): "amarillo",
    ("tamaño", "mediano"): "naranja",
    ("tamaño", "grande"): "violeta"
}

# Función para inferir el color de un objeto dado sus características
def inferir_color(caracteristicas):
    for regla, color in reglas.items():  # Iteramos sobre cada regla en el diccionario de reglas
        if regla[0] == caracteristicas[0] and regla[1] == caracteristicas[1]:  # Comparamos las características
            return color  # Si encontramos una regla que coincide, retornamos el color asociado
    return "color no definido"  # Si no encontramos una regla que coincida, retornamos un mensaje de error

# Ejemplo de uso
if __name__ == "__main__":
    # Características del objeto
    caracteristicas = ("forma", "redondo")

    # Inferimos el color del objeto utilizando las características dadas
    color = inferir_color(caracteristicas)

    # Imprimimos el resultado
    print(f"El color del objeto con características {caracteristicas} es: {color}")
