from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    comision = models.IntegerField()

    def __str__(self):
        return f'{self.nombre}'
    
class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    comision = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return f'{self.apellido}, {self.nombre}'

class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    profesion = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'
        ordering = ['-apellido']

    def __str__(self):
        return f'{self.apellido}, {self.nombre}'

class Entregable(models.Model):
    nombre = models.CharField(max_length=50)
    fechaEntrega = models.DateField()
    entegado = models.BooleanField()

    def __str__(self):
        return f"{self.fechaEntrega}"