# soluciones de hoja de ejercicios 3
import math

def ejercicio_1():
    num = int(input("Introduce un número:\t"))
    if num >= 0:
        print(num)


def ejercicio_2():
    num_1 = int(input("Introduce el primer número:\t"))
    num_2 = int(input("Introduce el segundo número:\t"))
    print(num_1, num_2)


def ejercicio_3():
    num = int(input("Introduce un número:\t"))
    if num > 0:
        print(num)
    else:
        print("siempre positivo, nunca negativo")


def ejercicio_4():
    num_1 = int(input("Introduce el primer número:\t"))
    num_2 = int(input("Introduce el segundo número:\t"))
    print(num_1 % num_2)


def ejercicio_5():
    num_1 = int(input("Introduce el primer número:\t"))
    num_2 = int(input("Introduce el segundo número:\t"))
    print(num_1 / num_2)


def ejercicio_6():
    num_1 = int(input("Introduce el primer número:\t"))
    num_2 = int(input("Introduce el segundo número:\t"))
    print(num_1 if num_1 < num_2 else num_2)


def ejercicio_7():
    num_1 = int(input("Introduce el primer número:\t"))
    num_2 = int(input("Introduce el segundo número:\t"))
    print(num_1 if num_1 > num_2 else num_2)


def ejercicio_8():
    num_1 = int(input("Introduce el primer número:\t"))
    num_2 = int(input("Introduce el segundo número:\t"))
    start = num_1 if num_1 < num_2 else num_2
    end = num_1 if num_1 > num_2 else num_2
    for i in range(start, end + 1):
        print(i)

def es_primo(num):
    if num <= 3:
        return True
    if num % 2 == 0:
        return False
    raiz = math.ceil(num**0.5)
    for i in range(3, raiz + 1, 2):
        if num % i == 0:
            return False
    return True


def ejercicio_9():
    num_1 = int(input("Introduce un número:\t"))
    for i in range(1, num_1 + 1):
        if es_primo(i):
            print(i)

#print(es_primo(9))
ejercicio_9()