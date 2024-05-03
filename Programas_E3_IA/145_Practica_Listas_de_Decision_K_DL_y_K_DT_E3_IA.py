# Practica_145_Listas_de_Decision_K_DL_y_K_DT_E3_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Listas_de_Decision_K_DL_y_K_DT

# Definición de la función para clasificar un ejemplo utilizando una lista de reglas
def decision_list_classify(example, decision_list):
    for condition, prediction in decision_list:
        if condition(example):
            return prediction
    return None  # Si ninguna regla coincide, se devuelve None

# Conjunto de datos de entrada
data = [
    ({'edad': 25, 'salario': 35000}, 'aprobado'),
    ({'edad': 30, 'salario': 45000}, 'aprobado'),
    ({'edad': 20, 'salario': 30000}, 'rechazado'),
    ({'edad': 35, 'salario': 50000}, 'aprobado'),
    ({'edad': 40, 'salario': 60000}, 'aprobado'),
    ({'edad': 45, 'salario': 70000}, 'aprobado'),
]

# Definición de una lista de reglas de ejemplo
decision_list = [
    (lambda x: x['edad'] < 30, 'rechazado'),  # Si la edad es menor que 30, se rechaza
    (lambda x: x['salario'] > 40000, 'aprobado'),  # Si el salario es mayor que 40000, se aprueba
    (lambda x: True, 'rechazado')  # En todos los demás casos, se rechaza
]

# Clasificación de ejemplos utilizando la lista de reglas
for example, _ in data:
    prediction = decision_list_classify(example, decision_list)
    print("Ejemplo:", example, "Predicción:", prediction)
