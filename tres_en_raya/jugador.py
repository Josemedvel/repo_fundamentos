from tablero import Tablero

class Jugador:

    def __init__(self):
        self.ficha = self.seleccionar_ficha()

    def seleccionar_ficha(self):
        ficha = ""

        while len(ficha) != 1:
            ficha = input("Ingresa el valor de una ficha válida")

        return ficha.upper()

    def recibir_coordenada(self, posicion):
        coor = -1
        while coor < 0 or coor > 2:
            try:
                coor = int(input(f"Ingrese un valor para la {posicion} entre 0 y 2:\t"))
            except Exception as e:
                print("No se ha ingresado un número")
        return coor
          
    def colocar_ficha(self, tablero:Tablero):
        x = self.recibir_coordenada("fila")
        y = self.recibir_coordenada("columna")
        
        while tablero.esta_ocupada(x,y):
            print("Esa casilla está ocupada")
            x = self.recibir_coordenada("fila")
            y = self.recibir_coordenada("columna")
        
        tablero.colocar_ficha(self.ficha, x, y)