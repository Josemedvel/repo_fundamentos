import random
jugadas = ["piedra", "papel", "tijeras"]
j_ord = jugadas[random.randint(0,2)]
j_jug = input("Elige entre piedra, papel o tijeras:")
print("El ordenador juega: " + j_ord)
if j_ord == j_jug:
    print("EMPATE")
elif (j_ord == "papel" and j_jug == "piedra") or (j_ord == "tijeras" and j_jug == "papel") or (j_ord == "piedra" and j_jug == "tijeras"):
    print("GANA ORDENADOR")
else:
    print("GANA JUGADOR")