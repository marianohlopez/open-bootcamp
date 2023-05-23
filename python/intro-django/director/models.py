from django.db import models


class Director(models.Model):
    nombre = models.CharField(max_length=100, help_text="Nombre del director")
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre


class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo
