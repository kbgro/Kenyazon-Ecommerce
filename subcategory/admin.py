from django.contrib import admin
from subcategory.models import SubCategory


# Register your models here.
class SubCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('subcategory_name',)}
    list_display = ('subcategory_name', 'slug', 'category')


admin.site.register(SubCategory, SubCategoryAdmin)
