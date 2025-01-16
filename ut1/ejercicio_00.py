# ejercicio 1
import random
def ejercicio_1(num_1, num_2, num_3):
    '''num_1 = int(input("Introduce el primer número: /n"))
    num_2 = int(input("Introduce el segundo número: /n"))
    num_3 = int(input("Introduce el tercer número: /n"))
    '''
    if num_1 < num_2:
        if num_2 < num_3:
            print(num_1, num_2, num_3)
        else:
            if num_1 < num_3:
                print(num_1, num_3, num_2)
            else:
                print(num_3, num_1, num_2)
    else: 
        if num_2 > num_3:
            print(num_3, num_2, num_1)
        else:
            if num_1 > num_3:
                print(num_2, num_3, num_1)
            else:
                print(num_2, num_1, num_3)

def ejercicio_2(lista):
    print(lista)
    num = int(input("Ingresa un valor a buscar /n"))
    for i, n in enumerate(lista):
        if n == num:
            return i
    return -1

ejercicio_1(5,10,15)
ejercicio_1(20,10,15)
ejercicio_1(20,15,10)
ejercicio_1(8,10,7)
ejercicio_1(5,20,15)
ejercicio_1(5,10,15)

lista = [random.randrange(start=0, stop=50) for _ in range(50)]
print(ejercicio_2(lista))