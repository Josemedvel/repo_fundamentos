diccionario = {}
with open("./archive/car_price_dataset.csv") as file:
    lineas = file.readlines()
    for linea in lineas:
        datos = linea.split(",")
        marca = datos[0]
        if marca == "Kia":
            if marca in diccionario:
                diccionario[marca] += 1
            else:
                diccionario[marca] = 1
print(diccionario)

with open("calculos_marcas.csv", "w") as out_file:
    resultado = ""
    for marca in diccionario:
        resultado = resultado + marca + "," + str(diccionario[marca]) + "\n"
    out_file.write(resultado)