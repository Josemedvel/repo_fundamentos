variable = 5
tupla = (1,2,3)
print(tupla[2])
lista = [5,6,7]
lista[1] = 10
print(lista[1])
print(lista)
lista_dos_dimensiones = [
    (1,2,3),
    [4,5,6],
    [7,8,9]
]
print(lista_dos_dimensiones)
# añadir elemento a la lista
lista.append(200)
print(lista) # [5, 10, 7, 200]
lista.pop(2)
print(lista)

def multiplos_tres_y_cinco(inicio, final):
    numeros = []
    for i in range(inicio, final + 1, 1):
        if i % 3 == 0 and i % 5 == 0:
            numeros.append(i)
    return numeros

print(multiplos_tres_y_cinco(1, 46))

def lista_por_teclado(n):
    numeros = []
    for i in range(n):
        numeros.append(input(f"Introduce el valor del índice {i}:\t"))
    return numeros

def lista_numeros_por_teclado(n):
    numeros = []
    for i in range(n):
        propuesta = input(f"Introduce el numero del índice {i}:\t")
        while not propuesta.isdecimal():
            propuesta = input(f"Introduce el numero del índice {i}:\t")
        numeros.append(int(propuesta))
    return numeros


print(lista_numeros_por_teclado(5))