# Practica_123_Ingeniería_del_Conocimiento_Ontologías_E3_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Ingeniería_del_Conocimiento_Ontologías

from rdflib import Graph, Literal, Namespace, RDF, URIRef

# Creamos un nuevo grafo RDF
g = Graph()

# Definimos dos namespaces para nuestros términos y propiedades
ex = Namespace("http://www.ejemplo.com/ontologia#")
foaf = Namespace("http://xmlns.com/foaf/0.1/")

# Agregamos algunas tripletas al grafo RDF
g.add((ex.Juan, RDF.type, foaf.Person))
g.add((ex.Juan, foaf.name, Literal("Juan")))
g.add((ex.Juan, foaf.age, Literal(30)))
g.add((ex.Juan, foaf.knows, ex.Maria))
g.add((ex.Maria, RDF.type, foaf.Person))
g.add((ex.Maria, foaf.name, Literal("Maria")))
g.add((ex.Maria, foaf.age, Literal(25)))

# Guardamos el grafo en un archivo RDF/XML
g.serialize("ontologia.rdf", format="xml")

# Imprimimos el grafo RDF
print(g.serialize(format="turtle").decode("utf-8"))

# Realizamos una consulta sobre el grafo
for s, p, o in g.triples((None, RDF.type, foaf.Person)):
    print(f"{s} es una persona.")

# Realizamos otra consulta sobre el grafo
for s, p, o in g.triples((None, foaf.age, None)):
    print(f"{s} tiene {o} años.")
