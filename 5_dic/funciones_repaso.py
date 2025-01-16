# Función que calcula el mayor número de una lista y lo devuelve
lista = [1,82, -4, 5]
def mayor_de_lista(lista):
    if len(lista) == 0:
        raise Exception("La lista está vacía")
    else:
        mayor = lista[0]
        for i in lista:
            if i > mayor:
                mayor = i
        return mayor
maximo = mayor_de_lista(lista)
print(maximo)

# Funcion que devuelve una lista de pares que están
#  dentro de una lista pasada como parámetro

def pares(lista):
    pares = []
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
    return pares

print(pares(lista))