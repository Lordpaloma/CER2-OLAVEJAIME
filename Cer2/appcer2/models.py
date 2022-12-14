from django.db import models

class Residencia(models.Model):
    numero  = models.IntegerField( primary_key=True)
    dueño = models.CharField(max_length=50)
    telefono = models.IntegerField()
    Correo = models.CharField(max_length=50)
    def __str__(self):
        return "Residencia "+str(self.numero)


class Correspondencia(models.Model):
    fecha_entrega = models.DateField("Fecha de recepción")
    Conserje = models.CharField(max_length=50, blank=True)
    entregado = models.BooleanField()
    destinatario = models.CharField(max_length=90)
    direccion = models.ForeignKey(Residencia, on_delete=models.CASCADE)
    def __int__(self):
        return str(self.direccion)