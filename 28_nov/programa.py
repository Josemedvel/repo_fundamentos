import matematicas as mt

def pedir_numero(letra=""):
    numero = float(input(f"Por favor, inserta un número para la variable '{letra}':"))
    return numero

def calcular_ecuacion_2_grado_interactiva():
    a = pedir_numero("a")
    b = pedir_numero("b")
    c = pedir_numero("c")
    print(f"{a}*X² + {b}*X + {c} = 0")
    resultado = mt.ecuacion2grado(a, b, c)
    print(resultado)



# calcular_ecuacion_2_grado_interactiva()

def es_anno_bisiesto(anno):
    if (anno % 4 == 0 and anno % 100 == 0) or anno % 400 == 0:
        return True
    else:
        return False
print(es_anno_bisiesto(pedir_numero()))