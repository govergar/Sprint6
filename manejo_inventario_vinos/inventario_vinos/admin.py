from django.contrib import admin
from .models import InventoryItem, Cepa, Tipo

admin.site.register(InventoryItem)
admin.site.register(Cepa)
admin.site.register(Tipo)
# Register your models here.
