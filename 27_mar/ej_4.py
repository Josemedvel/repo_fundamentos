import sys


archivo = sys.argv[1]
with open(archivo, "r") as file:
    texto = file.read()
    palabras = texto.split(" ")
    diccionario = {}
    minima_aparicion = 100
    palabra_menos_repetida = ""
    for palabra in palabras:
        if palabra in diccionario:
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1
        if diccionario[palabra] < minima_aparicion:
            minima_aparicion = diccionario[palabra]
            palabra_menos_repetida = palabra

if "hola" in diccionario:
    print(diccionario["hola"])
else:
    print("No hay 'hola' en el archivo")
print("La palabra menos repetida es: ", palabra_menos_repetida)