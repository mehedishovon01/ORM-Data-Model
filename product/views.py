from django.shortcuts import render
from .models import Category, Brand, Warranty, Seller, Product

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    brands = Brand.objects.all()
    warranty = Warranty.objects.all()
    seller = Seller.objects.all()

    context = {
        'products': products, 
        'categories': categories, 
        'brands': brands,
        'warranty': warranty,
        'sellers': seller,
        }

    return render(request, 'products.html', context)
