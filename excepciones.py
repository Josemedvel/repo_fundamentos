while True:
    try:
        numerador = int(input("ingrese un numerador:\t"))
        denominador = int(input("ingrese un denominador:\t"))
        division = numerador / denominador
        print(division)
    except Exception as error:
        print("Ha habido un error:", error)
        