fin = False
with open("salida.txt","w") as salida:
    while not fin:
        linea = input("Ingresa una línea para escribir en el archivo:\n")
        if linea == "FIN":
            fin = True
        salida.write(linea+"\n")
