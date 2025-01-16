# equivale a las soluciones de la hoja 1.2
from math import ceil
def ejercicio_1():
    num = int(input("Introduce un número:\n"))
    for i in range(num + 1):
        print(i)
def ejercicio_2():
    num_1 = int(input("Introduce el primer número:\t"))
    num_2 = int(input("Introduce el segundo número:\t"))
    if num_1 == num_2:
        print("iguales")
    else:
        print("distintos")
def ejercicio_3():
    num_1 = int(input("Introduce el primer número:\t"))
    num_2 = int(input("Introduce el segundo número:\t"))
    print(num_1 * num_2)
def ejercicio_4():
    num_1 = int(input("Introduce el primer número:\t"))
    num_2 = int(input("Introduce el segundo número:\t"))
    if num_1 % num_2 == 0:
        print("divisible")
    else:
        print("no divisible")
def ejercicio_5_raiz():
    num_1 = int(input("Introduce el primer número:\t"))
    raiz = ceil(num_1**(0.5))
    if num_1 % 2 == 0:
        return
    for i in range(3, raiz + 1, 2):
        print(i)
        if num_1 % i == 0:
            return
    print("El número es primo")

def ejercicio_5_total():
    num_1 = int(input("Introduce el primer número:\t"))
    if num_1 % 2 == 0:
        return
    for i in range(3, num_1, 2):
        print(i)
        if num_1 % i == 0:
            return
    print("El número es primo")

ejercicio_5_total()