# Ej 1: Haz una función que tenga 2 parámetros, ancho y alto,
#  e imprima un rectángulo con * de las medidas solicitadas

# Ej 2: Haz una función que dada una lista de nombres,
#  se pase por parámetro otro nombre y devuelva el número
#  de apariciones de ese nombre en la lista

lista = ["Juan", "Jose", "María", "Begoña", "Jose"]
def contar_apariciones_nombre(lista, nombre):
    resultado = 0
    for n in lista:
        if n == nombre:
            resultado += 1
    return resultado

        
def contar_apariciones_nombre_2(lista, nombre):
    resultado = 0
    for i in range(len(lista)):
        if lista[i] == nombre:
            resultado += 1
    return resultado

print(contar_apariciones_nombre(lista, "Jose"))

# Ej 3: Haz una función que calcule el número máximo de una lista
def maximo(lista):
    if len(lista) == 0:
        raise Exception("La lista está vacía")
    numero = lista[0]
    for n in lista:
        if numero < n:
            numero = n
    return numero
# Ej 4: Haz una función que calcule el número mínimo de una lista
def minimo(lista):
    if len(lista) == 0:
        raise Exception("La lista está vacía")
    numero = lista[0]
    for n in lista:
        if numero > n:
            numero = n
    return numero
# Ej 5: Haz una función que simule las tiradas de 5 dados y devuelva
#  la suma de las puntuciones, sin contar las tiradas
#  de más puntuación y las de menos puntuación

import random
def tirada(dados = 5):
    lista = []
    for i in range(dados):
        num_tirada = random.randint(1,6)
        lista.append(num_tirada)
    lista.remove(maximo(lista))
    lista.remove(minimo(lista))
    suma = 0
    for i in lista:
        suma = suma + i
    return suma