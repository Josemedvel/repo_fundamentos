import sys
if len(sys.argv) >= 2:
    with open(sys.argv[1], encoding="utf-8", mode="r") as archivo:
        texto_archivo = archivo.read().lower()
        num_letras = len(texto_archivo)
        lista_caracteres_limpiar = {
            "\n": " ",
            ".": "",
            ";": "",
            ",": "",
            "-": "",
            ":": "",
            "  ": " ",
            "¿": "",
            "?": "",
            "!": "",
            "¡": ""
        }
        for caracter in lista_caracteres_limpiar:
            texto_archivo = texto_archivo.replace(caracter, lista_caracteres_limpiar[caracter])
        palabras = texto_archivo.split(" ")
        diccionario_apariciones = {}
        


        for palabra in palabras:
            if len(palabra.strip()) != 0: 
                if palabra in diccionario_apariciones:
                    diccionario_apariciones[palabra] += 1
                else:
                    diccionario_apariciones[palabra] = 1
        palabra_mas_repetida = ["", 0]
        for palabra in diccionario_apariciones:
            if diccionario_apariciones[palabra] > palabra_mas_repetida[1]:
                palabra_mas_repetida[0] = palabra
                palabra_mas_repetida[1] = diccionario_apariciones[palabra]
    lista_mas_repetidas = []
    for i in range(20):
        palabra_mas_repetida = ["", 0]
        for palabra in diccionario_apariciones:
            if diccionario_apariciones[palabra] > palabra_mas_repetida[1]:
                palabra_mas_repetida[0] = palabra
                palabra_mas_repetida[1] = diccionario_apariciones[palabra]
        lista_mas_repetidas.append(palabra_mas_repetida)
        del(diccionario_apariciones[palabra_mas_repetida[0]])

    print(lista_mas_repetidas)
    print(f"Número de letras: {num_letras}")
    #print(f"Diccionario palabras: {diccionario_apariciones}")
    print(f"Palabra más repetida: {palabra_mas_repetida}")

with open("salida_quijote.txt", encoding="utf-8", mode="a") as salida:
    for palabra in diccionario_apariciones:
        salida.write(f"{palabra}-->{diccionario_apariciones[palabra]}\n")

