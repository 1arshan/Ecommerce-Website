from django.contrib import admin
from . import models
# Register your models here.


class ProductInline(admin.ModelAdmin):
    model = models.Product
    readonly_fields=('id',)

admin.site.register(models.Product,ProductInline)
admin.site.register(models.OrderItem)
admin.site.register(models.ShippingAddress)
admin.site.register(models.Purchased_item)
admin.site.register(models.FullOrder)

class ProductCategoriesInline(admin.ModelAdmin):
    model = models.ProductCategories
    readonly_fields=('id',)

admin.site.register(models.ProductCategories,ProductCategoriesInline)
