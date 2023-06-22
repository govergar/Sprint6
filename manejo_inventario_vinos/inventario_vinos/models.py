from django.db import models
from django.contrib.auth.models import User

# Create your models here.




class InventoryItem(models.Model):
	Nombre = models.CharField(max_length=200)
	Cepa = models.ForeignKey('Cepa', on_delete=models.SET_NULL, blank=True, null=True)
	Tipo = models.ForeignKey('Tipo', on_delete=models.SET_NULL, blank=True, null=True)
	Viña = models.CharField(max_length=200)
	Año = models.IntegerField()
	Cantidad = models.IntegerField()
	date_created = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
    
def __str__(self):
		return self.name

class Cepa(models.Model):
	Nombre = models.CharField(max_length=200)
	
def __str__(self):
		return self.name

class Tipo(models.Model):
	Nombre = models.CharField(max_length=200)
	
def __str__(self):
		return self.name
