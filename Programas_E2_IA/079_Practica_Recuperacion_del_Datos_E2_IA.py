# Practica_079_Recuperacion_del_Datos_E2_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Recuperacion_del_Datos

import pandas as pd

# Cargar datos desde un archivo CSV
df = pd.read_csv("datos.csv")

# Imprimir la estructura de datos
print("Estructura de datos:")
print(df)

# Obtener información sobre los datos
print("\nInformación sobre los datos:")
print(df.info())

# Mostrar las primeras filas de datos
print("\nPrimeras filas de datos:")
print(df.head())

# Realizar consultas a los datos
print("\nConsulta a los datos:")
# Seleccionamos solo las filas donde la columna 'edad' sea mayor que 30
resultados = df[df['edad'] > 30]
print(resultados)
