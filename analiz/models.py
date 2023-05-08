from django.db import models
from django.contrib.auth.models import User
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
    


class Sell(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False)
    price = models.IntegerField(default=0, null=False, blank=False)

    def __str__(self) -> str:
        return self.product.name




class Marketplace(models.Model):
    days = (
        ('Pazartesi', 'Pazartesi'),
        ('Salı', 'Salı'),
        ('Çarşamba', 'Çarşamba'),
        ('Perşembe', 'Perşembe'),
        ('Cuma', 'Cuma'),
        ('Cumartesi', 'Cumartesi'),
        ('Pazar', 'Pazar'),


    )
    marketplace_name = models.CharField(max_length=200)
    marketplace_addres =  models.CharField(max_length=300)
    lat = models.FloatField()
    long =  models.FloatField()
    day = models.CharField(max_length=20, choices=days)

    def __str__(self) -> str:
        return self.marketplace_name


# sell kısmında sadece selleri kendi olduğunu ekleyebilir
class PlaceOfSale(models.Model):
    days = (
        ('Pazartesi', 'Pazartesi'),
        ('Salı', 'Salı'),
        ('Çarşamba', 'Çarşamba'),
        ('Perşembe', 'Perşembe'),
        ('Cuma', 'Cuma'),
        ('Cumartesi', 'Cumartesi'),
        ('Pazar', 'Pazar'),
        )
    seller = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    marketplace = models.ForeignKey(Marketplace, on_delete=models.CASCADE, null=False, blank=False)
    products = models.ManyToManyField(Sell)
    day = models.CharField(max_length=20, choices=days)

    
    def __str__(self) -> str:
        return f"{self.marketplace}, {self.seller}, {self.day}"


# products kısmında sadece selleri kendi olduğunu ekleyebilir
class ProductProfit(models.Model):
    product = models.ForeignKey(Sell, on_delete=models.CASCADE, null=False, blank=False)
    profit = models.FloatField()
    unit_sales = models.IntegerField()

    def __str__(self) -> str:
        return self.product.product.name



# products kısmında sadece selleri kendi olduğunu ekleyebilir
class Revenue(models.Model):
    place_of_sale = models.ForeignKey(PlaceOfSale, on_delete=models.CASCADE, null=False, blank=False)
    ciro = models.FloatField()
    date = models.DateField()
    products = models.ManyToManyField(ProductProfit)
    def __str__(self) -> str:
        return f"{self.place_of_sale}, {self.ciro}, {self.date}"