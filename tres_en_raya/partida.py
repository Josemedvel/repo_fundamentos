from tablero import Tablero
from jugador import Jugador
import random


class Partida:
    def __init__(self):
        self.tablero = Tablero()
        self.jugador_1 = Jugador()
        self.jugador_2 = Jugador()
        self.primer_jugador = None
        self.segundo_jugador = None
        self.primer_turno()

    def turno(self, jugador):
        jugador.colocar_ficha(self.tablero)
        if self.hay_tres_en_raya(jugador.ficha):
            print("Enhorabuena jugador 1, has ganado")
            return True
        elif self.hay_empate():
            print("Empate, nadie gana")
            return True
        self.tablero.mostrar_tablero()
        return False
    
    def jugar(self):
        while True:
            if self.turno(self.primer_jugador):
                break
            if self.turno(self.segundo_jugador):
                break

    def hay_empate(self):
        cont = 0
        for fila in self.tablero.casillas:
            for numero in fila:
                if numero != "":
                    cont += 1
        if cont == len(self.tablero.casillas) * len(self.tablero.casillas[0]):
            return True
        else:
            return False
        
    
    def vertical(self, ficha):
        for c in range(len(self.tablero.casillas[0])):
            cont = 0
            for fila in range(len(self.tablero.casillas)):
                if self.tablero.casillas[fila][c] == ficha:
                    cont = cont + 1
            if cont == len(self.tablero.casillas):
                return True
        return False
    
    def horizontal(self, ficha):
        for fila in range(len(self.tablero.casillas)):
            cont = 0
            for c in range(len(self.tablero.casillas[0])):
                if self.tablero.casillas[fila][c] == ficha:
                    cont = cont + 1
            if cont == len(self.tablero.casillas[0]):
                return True
        return False
    
    def diagonal(self, ficha):
        diag_mayor = 0
        diag_menor = 0
        for i in range(len(self.tablero.casillas)):
            if self.tablero.casillas[i][i] == ficha:
                diag_mayor = diag_mayor + 1

        if diag_mayor == len(self.tablero.casillas):
            return True
        for i in range(len(self.tablero.casillas)):
            if self.tablero.casillas[len(self.tablero.casillas) - 1 - i][i] == ficha:
                diag_menor = diag_menor + 1
        if diag_menor == len(self.tablero.casillas):
            return True
        else:
            return False

    def hay_tres_en_raya(self, ficha):
        resultado = False
        if self.vertical(ficha):
            resultado = True
        elif self.horizontal(ficha):
            resultado = True
        elif self.diagonal(ficha):
            resultado = True
        return resultado

    def primer_turno(self):
        num = random.randint(0,1)
        if num == 0: # significa que el primer turno lo tendrá el jugador_1
            print(f"El primer jugador será el de la ficha: {self.jugador_1.ficha}")
            self.primer_jugador = self.jugador_1
            self.segundo_jugador = self.jugador_2
        else:
            print(f"El primer jugador será el de la ficha: {self.jugador_2.ficha}")
            self.primer_jugador = self.jugador_2
            self.segundo_jugador = self.jugador_1

partida = Partida()
partida.jugar()