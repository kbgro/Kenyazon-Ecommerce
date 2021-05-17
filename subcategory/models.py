from django.db import models
from django.urls import reverse

from category.models import Category

# Create your models here.


class SubCategory(models.Model):
    subcategory_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=255, blank=True)
    subcategory_image = models.ImageField(upload_to='photos/subcategories', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.subcategory_name

    class Meta:
        verbose_name_plural = 'Subcategories'

    def get_url(self):
        return reverse('products_by_subcategory', args=[self.slug])
