
'''
id = 1
nombre
curso
profesor
aula
'''
class Curso:
    def __init__(self, id, nombre, curso, profesor, aula):
        self.id = id
        self.nombre = nombre
        self.curso = curso
        self.profesor = profesor
        self.aula = aula

    def cambiar_nombre(self, nombre):
        self.nombre = nombre

    def cambiar_curso(self, curso):
        self.curso = curso
    
    def cambiar_profesor(self, profesor):
        if len(profesor) < 3:
            print("El nombre de un profesor no puede ser más corto de 3 letras")
        else:
            self.profesor = profesor

    def cambiar_aula(self, aula):
        self.aula = aula

    def __str__(self):
        return f"ID:{self.id}, NOMBRE: {self.nombre}, CURSO:{self.curso}, PROFESOR:{self.profesor}, AULA:{self.aula}"
curso_dibujo = Curso(1, "Dibujo artístico", "24/25", "Julio", "A237")
print(curso_dibujo)
curso_dibujo.cambiar_profesor("")
print(curso_dibujo)