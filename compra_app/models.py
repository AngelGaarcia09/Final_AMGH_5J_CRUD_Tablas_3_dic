from django.db import models

# Create your models here.
class Compra(models.Model):
    id_compra=models.PositiveIntegerField(primary_key=True)
    fecha_compra=models.DateField(null=False,blank=False)
    id_trabajador=models.PositiveIntegerField()
    id_troca=models.PositiveIntegerField()
    ganancias=models.DecimalField(max_digits=10, decimal_places=2)
    forma_de_pago=models.CharField(max_length=50)
    total=models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.id_compra