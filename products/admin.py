from django.contrib import admin
from . import models

class ProdcutsAdmin(admin.ModelAdmin):
  list_display = ("title", "price",)
#   list_display = ("image", "title", "price",)

admin.site.register(models.Product, ProdcutsAdmin)
