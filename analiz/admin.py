from django.contrib import admin
from .models import Product, Sell, Marketplace, PlaceOfSale, Revenue, ProductProfit


class MarketplaceAdmin(admin.ModelAdmin):
    list_filter = ('day',)  # 'day' alanına filtre ekledik



class PlaceOfSaleAdmin(admin.ModelAdmin):
    list_display = ("marketplace",'day', "seller")  #
    
class RevenueAdmin(admin.ModelAdmin):
    list_display = ("place_of_sale",'ciro', "date")  

class ProductProfitAdmin(admin.ModelAdmin):
    list_display = ("product",'profit')  

admin.site.register(Product)
admin.site.register(Sell)
admin.site.register(ProductProfit, ProductProfitAdmin)
admin.site.register(PlaceOfSale, PlaceOfSaleAdmin)
admin.site.register(Marketplace, MarketplaceAdmin)
admin.site.register(Revenue, RevenueAdmin)
