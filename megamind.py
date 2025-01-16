


colores = ["azul", "rojo", "marron", "morado", "amarillo", "verde", "granate", "turquesa"]
eleccion = []
salir_contador = 0
num_colores = 4

while salir_contador != num_colores:
    eleccion = input("Ingresa tus colores:\n").split(" ")
    for color in eleccion:
        if color in colores:
            salir_contador += 1
print(eleccion)