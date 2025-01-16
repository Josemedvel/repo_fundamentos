coche = {
    "modelo":"Mondeo",
    "num_bastidor": 927384952,
    "tipo_combustible": "Gasolina",
    "potencia_motor": 110,
    "num_puertas": 5,
    "num_km": 20000
}
lista_coches = []

def crear_coche(modelo, num_bast, tipo_comb, potencia,num_puertas,num_km=0):
    nuevo_coche = {}
    nuevo_coche["modelo"] = modelo
    nuevo_coche["num_bastidor"] = num_bast
    nuevo_coche["tipo_combustible"] = tipo_comb
    nuevo_coche["potencia_motor"] = potencia
    nuevo_coche["num_puertas"] = num_puertas
    nuevo_coche["num_km"] = num_km
    return nuevo_coche

nuevo_coche = crear_coche("Fiesta", 23462346, "Electrico", 100, 4)


print(nuevo_coche)

def conducir(coche):
    coche["num_km"] = coche["num_km"] + 1

for i in range(10):
    conducir(nuevo_coche)

print(nuevo_coche)