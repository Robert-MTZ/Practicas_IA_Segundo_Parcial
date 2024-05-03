# Practica_077_Modelo_Gramaticas_Probab_Independ_del_Contexto_E2_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Gramaticas_Probab_Independ_del_Contexto

import nltk
from nltk.grammar import Nonterminal, Production
from nltk.probability import FreqDist
from nltk.corpus import treebank

# Obtener las producciones del corpus Treebank
productions = []
for tree in treebank.parsed_sents():
    productions.extend(tree.productions())

# Calcular la frecuencia de cada producción
production_freq = FreqDist(productions)

# Crear una gramática probabilística
pcfg = nltk.PCFG(Nonterminal('S'), production_freq)

# Generar árboles sintácticos aleatorios
for _ in range(3):
    tree = pcfg.generate()
    print(tree)

