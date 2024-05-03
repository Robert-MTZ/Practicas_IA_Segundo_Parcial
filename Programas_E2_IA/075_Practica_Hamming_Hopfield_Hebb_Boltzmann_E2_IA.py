# Practica_075_Hamming_Hopfield_Hebb_Boltzmann_E2_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Hamming_Hopfield_Hebb_Boltzmann

def hamming_distance(seq1, seq2):
    # Asegúrate de que las secuencias tengan la misma longitud
    assert len(seq1) == len(seq2), "Las secuencias deben tener la misma longitud"
    
    # Calcula la distancia de Hamming contando las posiciones en las que las secuencias difieren
    distance = sum(c1 != c2 for c1, c2 in zip(seq1, seq2))
    return distance

seq1 = "101010"
seq2 = "100110"
print("Distancia de Hamming entre", seq1, "y", seq2, ":", hamming_distance(seq1, seq2))

