class Alumno:
    def __init__(self, nia, email, curso=1):
        self.nia = nia
        self.email = email
        self.curso = curso

    def promocionar(self):
        if self.curso == 2:
            print("El alumno ya está en 2º curso")
            return
        self.curso = 2

    def __str__(self):
        return f"NIA:{self.nia}, EMAIL:{self.email}, CURSO: {self.curso}"
    
nuevo_alumno = Alumno(23462323, "juanito@gmail.com")
print(nuevo_alumno)
nuevo_alumno.promocionar()
print(nuevo_alumno)
nuevo_alumno.promocionar()