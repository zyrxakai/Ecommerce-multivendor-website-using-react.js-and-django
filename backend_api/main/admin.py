from django.contrib import admin
from . import models

admin.site.register(models.Vendor)
admin.site.register(models.ProductCategory)
admin.site.register(models.product)
admin.site.register(models.Customer)
admin.site.register(models.Order)
admin.site.register(models.OrderItems)
admin.site.register(models.CustomerAddress)
admin.site.register(models.ProductRating)
