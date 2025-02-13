class Tablero:
    def __init__(self):
        self.casillas = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]
    
    def esta_ocupada(self, fila, columna):
        return self.casillas[fila][columna] != ""
    
    def mostrar_tablero(self):
        for fila in range(len(self.casillas)):
            for columna in range(len(self.casillas[fila])):
                if columna < len(self.casillas[fila]) - 1:
                    print(self.casillas[fila][columna], end="\t|\t")
                else:
                    print(self.casillas[fila][columna])
            if fila < len(self.casillas) - 1:
                print("-" * 35)
            else:
                print()
        
    def colocar_ficha(self, ficha, fila, columna): #asumimos que la posición y ficha son correctas
        self.casillas[fila][columna] = ficha