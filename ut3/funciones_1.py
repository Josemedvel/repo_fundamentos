def funcion_saludo(nombre):
    for i in range(5):
        print("Hola", nombre)

def suma(numero_1, numero_2):
    return numero_1 + numero_2

def multiplicacion(num_1, num_2):
    return num_1 * num_2

def n_veces_hola_buenas(n):
    for i in range(n):
        print("hola buenas")

def n_veces_una_cadena(n, cadena):
    for i in range(n):
        print(cadena)
#print(multiplicacion(suma(56, 89), suma(10,6)))
#n_veces_hola_buenas(2)
n_veces_una_cadena(3, "Hola buenas")
n_veces_una_cadena(4, "¿Qué tal estás?")