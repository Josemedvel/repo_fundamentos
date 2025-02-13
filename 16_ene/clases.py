class Alumno:
    def __init__(self, nia, email, curso=1):
        self.nia = nia
        self.email = email
        self.curso = curso
        self.partes = 0
        self.matriculas = []

    def matricular(self, nombre_curso):
        for m in self.matriculas:
            if m == nombre_curso:
                print("El alumno ya está matriculado")
                return
        self.matriculas.append(nombre_curso)
        print(f"El alumno acaba de ser matriculado en {nombre_curso}")
    
    def mostrar_matriculas(self):
        print()
        print("=" * 30)
        print(self.nia)
        print("=" * 30)
        for m in self.matriculas:
            print(m)
            print("-" * 30)
        

    def promocionar(self):
        if self.curso == 2:
            print("El alumno ya está en 2º curso")
            return
        self.curso = 2

    def poner_parte(self,gravedad):
        if gravedad == "leve":
            self.partes += 1
        elif gravedad == "grave":
            self.partes += 3
        elif gravedad == "muy_grave":
            self.partes += 5
        else: # en el caso de que no sea ni leve, ni grave ni muy grave, se va
            return
        if self.partes >= 5:
            print("El alumno ha sido expulsado")
            self.partes = 0

    def cambiar_correo(self, email):
        self.email = email

    def __str__(self):
        return f"NIA:{self.nia}, EMAIL:{self.email}, CURSO: {self.curso}, NºPARTES: {self.partes}"
    
nuevo_alumno = Alumno(23462323, "juanito@gmail.com")
print(nuevo_alumno)
nuevo_alumno.promocionar()
print(nuevo_alumno)
nuevo_alumno.promocionar()
nuevo_alumno.cambiar_correo("Xx__jovellanos__xX@gmail.com")
print(nuevo_alumno)
nuevo_alumno.poner_parte("leve")
print(nuevo_alumno)
nuevo_alumno.poner_parte("muy_grave")
print(nuevo_alumno)
nuevo_alumno.poner_parte("leve")
print(nuevo_alumno)


nuevo_alumno.matricular("Matemáticas")
nuevo_alumno.matricular("Lengua")
nuevo_alumno.matricular("Inglés")
nuevo_alumno.matricular("Programación")
nuevo_alumno.matricular("Matemáticas")

nuevo_alumno.mostrar_matriculas()