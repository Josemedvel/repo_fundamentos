class Ascensor:
    def __init__(self, piso_max, piso_min, piso_actual, pers_max):
        self.piso_max = piso_max
        self.piso_min = piso_min
        self.piso_actual = piso_actual
        self.personas_max = pers_max
        self.personas_actual = 0

    def subir_piso(self):
        if self.piso_actual != self.piso_max:
            self.piso_actual += 1
            self.mostrar_piso()
            self.mostrar_personas_actuales()
    
    def bajar_piso(self):
        if self.piso_actual != self.piso_min:
            self.piso_actual -= 1
            self.mostrar_piso()
            self.mostrar_personas_actuales()

    def ir_a_piso(self, objetivo):
        if self.piso_actual != objetivo and objetivo in range(self.piso_min, self.piso_max + 1):
            diferencia_pisos = self.piso_actual - objetivo
            if diferencia_pisos > 0: # bajamos
                for i in range(diferencia_pisos):
                    self.bajar_piso()
            else:
                for i in range(diferencia_pisos * -1):
                    self.subir_piso()
    
    def esta_lleno(self):
        return self.personas_actual == self.personas_max
    
    def esta_vacio(self):
        return self.personas_actual == 0

    def bajar_persona(self):
        if not self.esta_vacio():
            self.personas_actual -= 1

    def subir_persona(self):
        if not self.esta_lleno():
            self.personas_actual += 1

    def subir_personas(self, personas_esperando):
        if not self.esta_lleno():
            entrarian = self.personas_max - self.personas_actual
            if entrarian > personas_esperando:
                entran = personas_esperando
            else:
                entran = entrarian
            for i in range(entran):
                self.subir_persona()

    def subir_personas_v2(self, personas_esperando):
        while not self.esta_lleno() and personas_esperando > 0:
            self.subir_persona()
            personas_esperando -= 1
    
    def mostrar_piso(self):
        print("Estamos en el piso:", self.piso_actual)
    
    def mostrar_personas_actuales(self):
        print("Hay un total de ", self.personas_actual, "en el ascensor")

    def mostrar_informacion_actual(self):
        self.mostrar_piso()
        self.mostrar_personas_actuales()

class Menu:
    def __init__(self, ascensor):
        self.ascensor = ascensor

    def menu_inicial(self):
        print("MENU PRINCIPAL")
        print("1. Subir una persona")
        print("2. Bajar una persona")
        print("3. Ir a un piso")
        print("4. Subir X personas")
        print("5. Imprimir información actual")
        num = input("Presione enter para continuar:\t")
        if num.isdigit() and int(num) in range(1,6):
            return int(num)
        else:
            print("Por favor, introduzca un número válido")
            return self.menu_inicial()
        
    def menu_ir_a_piso(self):
        piso = None
        while piso == None:
            print("Menú ir a un piso")        
            num = input(f"Por favor, introduzca un piso al que ir, debe estar entre {self.ascensor.piso_min} y {self.ascensor.piso_max}:\t")
            if num.isdigit() and int(num) >= self.ascensor.piso_min and int(num) <= self.ascensor.piso_max:
                piso = int(num)
            else:
                print("Por favor, introduzca un número válido")
        return piso

    def menu_subir_personas(self):
        personas = None
        while personas == None:
            print("Menú subir personas")
            num = input(f"Por favor, introduzca el número de personas a subir, debe ser un número entero positivo:\t")
            if num.isdigit() and int(num) > 0:
                personas = int(num)
            else:
                print("Por favor, introduzca un número válido")
        return personas


ascensor = Ascensor(5,0,0,10)
menu = Menu(ascensor)

while True:
    opcion = menu.menu_inicial()
    if opcion == 1:
        ascensor.subir_persona()
    elif opcion == 2:
        ascensor.bajar_persona()
    elif opcion == 3:
        piso = menu.menu_ir_a_piso()
        ascensor.ir_a_piso(piso)
    elif opcion == 4:
        personas = menu.menu_subir_personas()
        ascensor.subir_personas_v2(personas)
    elif opcion == 5:
        ascensor.mostrar_informacion_actual()