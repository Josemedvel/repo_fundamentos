import random


def ejercicio_1(lista):  # sin enumerate
    longitud = len(lista)
    for n in range(longitud):
        if lista[n] % 2 == 0:
            print(f"{lista[n]}, en la posición {n}, es par")
        else:
            print(lista[n], "es impar")


def ejercicio_2():
    entrada = ""
    suma = 0
    while not entrada.upper() == "F":
        entrada = input("introduce un número a sumar: \n")
        if entrada.upper() == "F":
            continue
        else:
            try:
                suma += int(entrada)
            except Exception:
                print(Exception("entrada no valida"))
    print(suma)


def ejercicio_3():
    try:
        num = int(input("introduce un número por favor:\n"))
        for x in range(num + 1):
            print(x, end="\t")
        print()
    except ValueError:
        print(ValueError("ha habido un error"))


def ejercicio_4():
    try:
        num = int(input("introduce un número por favor:\n"))
        for x in range(num + 1):
            if x % 2 != 0:
                print(x, end="\t")
        print()
    except ValueError:
        print(ValueError("ha habido un error"))


lista = [random.randrange(start=0, stop=50) for _ in range(10)]
ejercicio_1(lista)
# ejercicio_2()
ejercicio_3()
ejercicio_4()