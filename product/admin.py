from django.contrib import admin
from .models import Category, Brand, Warranty, Seller, Product

# Define this class for list_display and details
class CategoryDetails(admin.ModelAdmin):
    """
    This class is for display the field in the Django admin interface and from details
    """
    list_display = ('name',)
    readonly_fields = ('created_at', 'updated_at',)

class BrandDetails(admin.ModelAdmin):
    """
    This class is for display the field in the Django admin interface and from details
    """
    list_display = ('name',)
    readonly_fields = ('created_at', 'updated_at',)

class WarrantyDetails(admin.ModelAdmin):
    """
    This class is for display the field in the Django admin interface and from details
    """
    list_display = ('duration',)
    readonly_fields = ('created_at', 'updated_at',)

class SellerDetails(admin.ModelAdmin):
    """
    This class is for display the field in the Django admin interface and from details
    """
    list_display = ('name',)
    readonly_fields = ('created_at', 'updated_at',)

class ProductDetails(admin.ModelAdmin):
    """
    This class is for display the field in the Django admin interface and from details
    """
    list_display = ('name', 'price', 'created_by')
    readonly_fields = ('created_at', 'updated_at',)


''' Registered models are here '''
admin.site.register(Category, CategoryDetails)
admin.site.register(Brand, BrandDetails)
admin.site.register(Warranty, WarrantyDetails)
admin.site.register(Seller, SellerDetails)
admin.site.register(Product, ProductDetails)