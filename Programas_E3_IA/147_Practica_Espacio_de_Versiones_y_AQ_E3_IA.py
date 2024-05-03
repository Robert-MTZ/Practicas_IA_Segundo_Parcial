# Practica_147_Espacio_de_Versiones_y_AQ_E3_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Espacio_de_Versiones_y_AQ

# Definición de la función de clasificación basada en la hipótesis
def classify(example, hypothesis):
    for attribute, value in example.items():
        if attribute not in hypothesis or hypothesis[attribute] != value:
            return None  # Si alguna característica no coincide, devuelve None
    return hypothesis['class']  # Si todas las características coinciden, devuelve la clase

# Función para generar la hipótesis inicial
def initial_hypothesis(X_train, y_train):
    hypothesis = {}  # Inicializamos la hipótesis como un diccionario vacío
    for example, label in zip(X_train, y_train):
        # Iteramos sobre cada ejemplo y su etiqueta de clase
        for attribute, value in example.items():
            # Iteramos sobre cada atributo y su valor en el ejemplo
            if attribute not in hypothesis:
                # Si el atributo no está en la hipótesis, lo agregamos con el valor del ejemplo
                hypothesis[attribute] = value
            elif hypothesis[attribute] != value:
                # Si el valor del atributo en la hipótesis no coincide con el valor del ejemplo, lo cambiamos a '?'
                hypothesis[attribute] = '?'
        # Asignamos la etiqueta de clase al atributo 'class' en la hipótesis
        hypothesis['class'] = label
    return hypothesis

# Conjunto de datos de entrenamiento
X_train = [
    {'edad': 'joven', 'ingreso': 'bajo', 'credito': 'bueno'},
    {'edad': 'joven', 'ingreso': 'bajo', 'credito': 'malo'},
    {'edad': 'joven', 'ingreso': 'medio', 'credito': 'bueno'},
    {'edad': 'joven', 'ingreso': 'alto', 'credito': 'malo'},
    {'edad': 'viejo', 'ingreso': 'alto', 'credito': 'malo'}
]
y_train = ['aprobado', 'rechazado', 'aprobado', 'rechazado', 'rechazado']

# Generamos la hipótesis inicial
initial_hyp = initial_hypothesis(X_train, y_train)

# Imprimimos la hipótesis inicial
print("Hipótesis inicial:", initial_hyp)

# Realizamos predicciones sobre los mismos datos de entrenamiento
predictions = [classify(example, initial_hyp) for example in X_train]

# Imprimimos las predicciones
print("Predicciones:", predictions)
