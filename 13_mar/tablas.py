resultado = ""

for i in range(1, 11):
    for j in range(1, 11):
        resultado = resultado + f"{i} x {j} = {i*j}\n"
    resultado = resultado + "\n"

with open("tablas.txt", "w") as fichero_salida:
    fichero_salida.write(resultado)

print("El archivo se ha escrito")