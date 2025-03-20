import sys
lista_argumentos = sys.argv

#print(lista_argumentos)
lista_argumentos.pop(0)
#print(lista_argumentos)

if len(lista_argumentos) < 2:
    print("Hay que introducir dos rutas válidas, no has puesto suficientes parámetros")
    sys.exit()

datos_a_copiar = None

with open(lista_argumentos[0], "rb") as archivo_inicial:
    datos_a_copiar = archivo_inicial.read()
    print("Se ha leído el archivo completo")

with open(lista_argumentos[1], "wb") as archivo_destino:
    archivo_destino.write(datos_a_copiar)
    print("Se ha escrito el archivo destino")



