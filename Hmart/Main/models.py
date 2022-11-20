from django.db import models
from django.urls import reverse


class ProductModel(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    photo = models.ImageField(upload_to="products_image")
    quantity = models.PositiveIntegerField()
    time_create = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    category = models.ForeignKey('CategoryModel', on_delete=models.PROTECT, null=True)
    brand = models.ForeignKey('BrandModel', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('single_product', kwargs={'product_id': self.pk})


class CategoryModel(models.Model):
    title = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.title


class BrandModel(models.Model):
    title = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.title