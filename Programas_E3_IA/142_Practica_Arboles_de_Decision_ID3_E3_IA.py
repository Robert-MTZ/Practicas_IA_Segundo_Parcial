# Practica_142_Arboles_de_Decision_ID3_E3_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Arboles_de_Decision_ID3

import numpy as np

# Definimos la clase del nodo del árbol de decisión
class NodoDecision:
    def __init__(self, atributo=None, valor=None, resultado=None):
        self.atributo = atributo  # Atributo utilizado para la división
        self.valor = valor  # Valor del atributo utilizado para la división
        self.resultado = resultado  # Resultado (clase) si es una hoja del árbol
        self.hijos = {}  # Diccionario de hijos del nodo

# Definimos la función para calcular la entropía
def calcular_entropia(datos):
    clases, conteos = np.unique(datos[:, -1], return_counts=True)
    probabilidades = conteos / len(datos)
    entropia = -np.sum(probabilidades * np.log2(probabilidades))
    return entropia

# Definimos la función para calcular la ganancia de información
def calcular_ganancia(datos, atributo):
    entropia_total = calcular_entropia(datos)
    valores, conteos = np.unique(datos[:, atributo], return_counts=True)
    peso_valores = conteos / np.sum(conteos)
    entropia_atributo = np.sum(peso_valores * calcular_entropia(datos[datos[:, atributo] == valor]))
    ganancia = entropia_total - entropia_atributo
    return ganancia

# Definimos la función para seleccionar el mejor atributo para la división
def seleccionar_atributo(datos):
    num_atributos = datos.shape[1] - 1
    ganancias = [calcular_ganancia(datos, atributo) for atributo in range(num_atributos)]
    mejor_atributo = np.argmax(ganancias)
    return mejor_atributo

# Definimos la función principal para construir el árbol de decisión
def construir_arbol(datos, etiquetas):
    # Verificamos si todos los datos tienen la misma etiqueta
    if len(np.unique(datos[:, -1])) == 1:
        return NodoDecision(resultado=np.unique(datos[:, -1])[0])

    # Si no, seleccionamos el mejor atributo para la división
    mejor_atributo = seleccionar_atributo(datos)
    nodo = NodoDecision(atributo=mejor_atributo)

    # Dividimos los datos en subconjuntos según el mejor atributo
    valores_atributo = np.unique(datos[:, mejor_atributo])
    for valor in valores_atributo:
        datos_subset = datos[datos[:, mejor_atributo] == valor]
        nodo.hijos[valor] = construir_arbol(datos_subset, etiquetas)

    return nodo

# Función para imprimir el árbol de decisión
def imprimir_arbol(arbol, espacio=""):
    if arbol.resultado is not None:
        print(espacio + "Resultado:", arbol.resultado)
        return
    print(espacio + "Atributo:", arbol.atributo)
    for valor, hijo in arbol.hijos.items():
        print(espacio + "   " + valor)
        imprimir_arbol(hijo, espacio + "   ")

# Creamos un conjunto de datos de ejemplo
datos = np.array([
    ['Soleado', 'Caluroso', 'Alta', 'No'],
    ['Soleado', 'Caluroso', 'Alta', 'No'],
    ['Nublado', 'Caluroso', 'Alta', 'Sí'],
    ['Lluvioso', 'Templado', 'Alta', 'Sí'],
    ['Lluvioso', 'Frío', 'Normal', 'Sí'],
    ['Lluvioso', 'Frío', 'Normal', 'No'],
    ['Nublado', 'Frío', 'Normal', 'Sí'],
    ['Soleado', 'Templado', 'Alta', 'No'],
    ['Soleado', 'Frío', 'Normal', 'Sí'],
    ['Lluvioso', 'Templado', 'Normal', 'Sí'],
    ['Soleado', 'Templado', 'Normal', 'Sí'],
    ['Nublado', 'Templado', 'Alta', 'Sí'],
    ['Nublado', 'Caluroso', 'Normal', 'Sí'],
    ['Lluvioso', 'Templado', 'Alta', 'No']
])

# Definimos las etiquetas de los atributos
etiquetas = ['Tiempo', 'Temperatura', 'Humedad', 'Jugar']

# Construimos el árbol de decisión
arbol_decision = construir_arbol(datos, etiquetas)

# Imprimimos el árbol de decisión
print("Árbol de Decisión:")
imprimir_arbol(arbol_decision)
