archivo = open("./archive/car_price_dataset.csv")
linea = None
diccionario = {}
archivo.readline()
while linea != "":
    linea = archivo.readline()
    datos = linea.split(",")
    marca = datos[0]
    if marca != "":
        if marca in diccionario: 
            diccionario[marca] += 1
        else:
            diccionario[marca] = 1
print(diccionario)
archivo.close()