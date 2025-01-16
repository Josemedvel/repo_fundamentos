n = int(input("Introduce un número entero:\t"))
suma_parcial = 0
for i in range(n+1):
    suma_parcial += i
print("El resultado es: " + str(suma_parcial))