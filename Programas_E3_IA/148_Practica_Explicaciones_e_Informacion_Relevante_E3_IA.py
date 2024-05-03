# Practica_148_Explicaciones_e_Informacion_Relevante_E3_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Explicaciones_e_Informacion_Relevante

# Definición de una función para obtener la importancia de las características
def feature_importance(model, X_train):
    # Calculamos el peso de cada característica basado en su importancia en el modelo
    importances = model.coef_[0]
    feature_names = X_train.columns
    
    # Creamos un diccionario para almacenar la importancia de cada característica
    feature_importance_dict = {}
    for feature_name, importance in zip(feature_names, importances):
        feature_importance_dict[feature_name] = importance
        
    return feature_importance_dict

# Conjunto de datos de entrenamiento
import pandas as pd
from sklearn.linear_model import LogisticRegression

# Creamos un DataFrame de ejemplo
data = {
    'edad': [25, 30, 20, 35, 40],
    'ingreso': [35000, 45000, 30000, 50000, 60000],
    'credito': [1, 0, 1, 0, 0],  # 1 para bueno, 0 para malo
    'aprobado': [1, 1, 0, 1, 1]   # 1 para aprobado, 0 para rechazado
}
df = pd.DataFrame(data)

# Dividimos el DataFrame en atributos (X) y etiquetas de clase (y)
X_train = df[['edad', 'ingreso', 'credito']]
y_train = df['aprobado']

# Creamos un modelo de regresión logística y lo entrenamos
model = LogisticRegression()
model.fit(X_train, y_train)

# Calculamos la importancia de las características utilizando la función definida
feature_importance_dict = feature_importance(model, X_train)

# Imprimimos la importancia de cada característica
print("Importancia de las características:")
for feature, importance in feature_importance_dict.items():
    print(f"{feature}: {importance}")
