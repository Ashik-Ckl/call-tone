from django.contrib import admin
from .import models
# Register your models here.


admin.site.register(models.category_image)
admin.site.register(models.brand)
admin.site.register(models.product_model)
admin.site.register(models.product)