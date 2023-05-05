from django.db import models

# Create your models here.



class Product(models.Model):
    Birim = (
        ('Kilogram', 'Kilogram'),
        ('Adet', 'Adet'),
        ('Sandık', 'Sandık'),
        ('Kutu', 'Kutu'),
        ('Demet', 'Demet'),

    )
    Kategori = (
        ('meyve', 'Meyve'),
        ('sebze', 'Sebze'),
        ('ithal', 'İthal Ürünler'),
    )
    name = models.CharField(max_length=200)
    birim = models.CharField(max_length=20, choices=Birim)
    kategori = models.CharField(max_length=20, choices=Kategori)


    def __str__(self) -> str:
        return self.name
    








