
lista = [1,3,5,5,7,2] # N = 6

def numero_mas_repetido_lista(lista):
    numero_mas_repetido = None
    numero_maximas_repeticiones = 0
    diccionario_numeros = {}
    for num in lista:
        if num in diccionario_numeros:
            diccionario_numeros[num] = diccionario_numeros[num] + 1
        else:
            diccionario_numeros[num] = 1
        if diccionario_numeros[num] > numero_maximas_repeticiones:
            numero_mas_repetido = num
            numero_maximas_repeticiones = diccionario_numeros[num]

    return [numero_mas_repetido, numero_maximas_repeticiones]


# print(numero_mas_repetido_lista(lista))


def numero_mas_repetido_lista_2(lista):
    numero_mas_repetido = None
    numero_maximas_repeticiones = 0
    for num in lista:
        numero_ocurrencias = 0
        for num_2 in lista:
            if num_2 == num:
                numero_ocurrencias += 1
        if numero_ocurrencias > numero_maximas_repeticiones:
            numero_mas_repetido = num
            numero_maximas_repeticiones = numero_ocurrencias
    return [numero_mas_repetido, numero_maximas_repeticiones]

print(numero_mas_repetido_lista_2(lista))
