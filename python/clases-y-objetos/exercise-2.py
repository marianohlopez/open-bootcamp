class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimirDatos(self):
        print(f"Nombre: {self.nombre}\nNota: {self.nota}")

    def aprobo(self):
        if self.nota < 7:
            print(f"El alumno {self.nombre} desaprobo")
        else:
            print(f"El alumno {self.nombre} aprobo con calificacion: {self.nota}")

alumn = Alumno("carlos", 6)

alumn.aprobo()