from django.contrib import admin
from products.models import Product, Variation


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}
    list_display = ('product_name', 'slug', 'price', 'stock', 'is_available')


admin.site.register(Product, ProductAdmin)


class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('product', 'variation_category', 'variation_value')


admin.site.register(Variation, VariationAdmin)
