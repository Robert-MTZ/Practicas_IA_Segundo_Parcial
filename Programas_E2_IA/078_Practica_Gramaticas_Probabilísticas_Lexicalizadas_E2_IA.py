# Practica_078_Gramaticas_Probabilísticas_Lexicalizadas_E2_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Gramaticas_Probabilísticas_Lexicalizadas

import nltk
from nltk.grammar import Nonterminal, Production
from nltk.probability import FreqDist
from nltk.corpus import treebank

# Obtener las producciones del corpus Treebank
productions = []
for tree in treebank.parsed_sents():
    productions.extend(tree.productions())

# Calcular la frecuencia de cada producción y de cada palabra terminal
production_freq = FreqDist(productions)
word_freq = FreqDist(treebank.words())

# Crear una gramática probabilística lexicalizada
lpcfg = nltk.LPCFG(Nonterminal('S'), production_freq, word_freq)

# Generar árboles sintácticos aleatorios
for _ in range(3):
    tree = lpcfg.generate()
    print(tree)

