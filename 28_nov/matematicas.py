import math
def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

def ecuacion2grado(a, b, c):
    if a == 0:
        raise Exception("No podemos dividir por 0")
    x1 = (-b + ((b**2 - 4*a*c)**0.5)) / (2*a)
    x2 = (-b - ((b**2 - 4*a*c)**0.5)) / (2*a)
    return (x1, x2)

if __name__ == "__main__":
    print(suma(1, 2))
    print(resta(1, 2))
    print(multiplicacion(1, 2))
    print(division(1, 2))
    print(ecuacion2grado(1, 2, 0))
