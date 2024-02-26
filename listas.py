"""
semana_laboral=["Lunes","Martes","Miércoles","Jueves","Viernes"]
print("Semana laboral =",semana_laboral)
print("Dia 1 =", semana_laboral[0])
print("Dia 2 =",semana_laboral[1])
print("Dia 3 =",semana_laboral[2])
print("Dia 4 =",semana_laboral[3])
print("Dia 5 =",semana_laboral[4])


"""
"""
carpeta_nombre= "C:\\Users\\Colibecas\\optativa_PLN\\"
archivo_nombre="Informacion_del_ordenador_PLN.txt"


with open(carpeta_nombre + archivo_nombre, "r") as archivo:
    texto = archivo.read() 

palabras_lista = texto.split() 
palabras_lista.sort() 

for palabra in palabras_lista: 
    print(palabra) 

espera = input("")
"""

#### otro codigo

"""
carpeta_nombre= "C:\\Users\\Colibecas\\optativa_PLN\\"
archivo_nombre="Informacion_del_ordenador_PLN.txt"


with open(carpeta_nombre+archivo_nombre,"r") as archivo:
    texto = archivo.read()
simbolos = ["(", ")", ".", ",", ":"]

for simbolo in simbolos:
    texto=texto.replace(simbolo," "+ simbolo + " ")


palabras_lista=texto.split()
palabras_lista.sort()
for palabra in palabras_lista:
    print(palabra)

"""
############    fin #####


#### otro codigo

import re

carpeta_nombre= "C:\\Users\\Colibecas\\optativa_PLN\\"
archivo_nombre="archivotexto.txt"


with open(carpeta_nombre+archivo_nombre,"r", encoding="utf-8") as archivo:
    texto = archivo.read()

#expresion_regu = re.compile(r"MA.*")
expresion_regu = re.compile(r"\bPr\w*")
#expresion_regu = re.compile(r"\w*e\b")
#expresion_regu = re.compile(r"\b\w*to\w*\b")
expresion_regu = re.compile(r"\b\w{5}\b")



#resultado_busqueda=expresion_regu.search(texto)

resultado_busqueda = expresion_regu.finditer(texto)


for coincidencia in resultado_busqueda:
    print(coincidencia.group(0))

input=("")
#print(resultado_busqueda.group(0))


