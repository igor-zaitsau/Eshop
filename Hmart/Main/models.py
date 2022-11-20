from django.db import models

class ProductModel(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    photo = models.ImageField(upload_to="products_image")
    quantity = models.PositiveIntegerField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title