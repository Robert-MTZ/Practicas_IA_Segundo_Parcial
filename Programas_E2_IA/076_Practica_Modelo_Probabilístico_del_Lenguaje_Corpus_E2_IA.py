# Practica_076_Modelo_Probabilístico_del_Lenguaje_Corpus_E2_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Modelo_Probabilístico_del_Lenguaje_Corpus

from collections import defaultdict

class LanguageModel:
    def __init__(self):
        self.word_counts = defaultdict(int)  # Diccionario para almacenar las frecuencias de palabras
        self.total_words = 0  # Total de palabras en el corpus

    def train(self, corpus):
        for sentence in corpus:
            for word in sentence.split():
                self.word_counts[word] += 1
                self.total_words += 1

    def word_probability(self, word):
        # Calcula la probabilidad de una palabra en el corpus
        return self.word_counts[word] / self.total_words if self.total_words > 0 else 0

    def sentence_probability(self, sentence):
        # Calcula la probabilidad de una secuencia de palabras en el corpus
        probability = 1.0
        for word in sentence.split():
            probability *= self.word_probability(word)
        return probability

corpus = [
    "el gato come pescado",
    "el perro juega en el parque",
    "el gato juega con el perro"
]

# Creamos una instancia del modelo de lenguaje
lm = LanguageModel()

# Entrenamos el modelo con el corpus
lm.train(corpus)

# Calculamos la probabilidad de una palabra
word = "gato"
print("Probabilidad de la palabra '{}' en el corpus:".format(word), lm.word_probability(word))

# Calculamos la probabilidad de una oración
sentence = "el gato juega"
print("Probabilidad de la oración '{}' en el corpus:".format(sentence), lm.sentence_probability(sentence))
