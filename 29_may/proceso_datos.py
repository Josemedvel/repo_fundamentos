class Tabla:
    def __init__(self):
        self.cabecera = None
        self.registros = []
    
    def leerCSV(self,nombre_fichero, cabecera=False):
        self.registros = []
        self.cabecera = []
        with open(nombre_fichero, "r") as fichero:
            lineas = fichero.readlines()
            lineas_limpias = []
            for linea in lineas:
                lineas_limpias.append(linea.strip()) # el método strip quita los saltos de línea de los finales de cadena
            if cabecera and len(lineas_limpias) >= 1:
                valor_cabecera = lineas_limpias.pop(0)
                self.cabecera = valor_cabecera.split(",")
                for l in lineas_limpias:
                    self.registros.append(l.split(","))
            else:
                self.cabecera = []
                for l in lineas_limpias:
                    self.registros.append(l.split(","))
        
    def __str__(self):
        return f"Tabla:\nCabecera: {self.cabecera}\nRegistros:\n{self.registros}"
    
tabla = Tabla()
tabla.leerCSV("datos_clientes.csv", cabecera=True)
print(tabla)
