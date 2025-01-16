import random
nombres = ["jose", "marcos", "juan", "fernando", "ana", "marta", "maría"]
apellidos = ["medina", "guerrero", "díaz", "gonzález", "martínez", "torres"]
def crear_nombre_completo(nombres, apellidos):
    nombre = nombres[random.randint(0,len(nombres) - 1)] # hasta aqui ok
    lista_copia_apellidos = apellidos.copy()
    random.shuffle(lista_copia_apellidos)
    apellido_1 = lista_copia_apellidos.pop()
    apellido_2 = lista_copia_apellidos.pop()
    return nombre + " " + apellido_1 + " " + apellido_2
for i in range(5):
    print(crear_nombre_completo(nombres, apellidos))


