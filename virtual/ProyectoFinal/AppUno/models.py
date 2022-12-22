from django.db import models

class Primos(models.Model):
    Nombre = models.CharField(max_length=50)
    Edad = models.IntegerField()

    def __str__(self):
        return f"{self.Nombre} - {str(self.Edad)}"

class Padres(models.Model):
    Nombre = models.CharField(max_length=50)
    Edad = models.IntegerField()

class Abuelos(models.Model):
    Nombre = models.CharField(max_length=50)
    Edad = models.IntegerField()
