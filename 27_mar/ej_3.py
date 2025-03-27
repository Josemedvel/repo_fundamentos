nombre_comp = input("Ingresa el nombre completo:")
separado = nombre_comp.split(" ")
with open("usuarios.txt", "a") as usuarios:
    usuarios.write(f"{separado[0]}, {separado[1]}, {separado[2]}\n")
