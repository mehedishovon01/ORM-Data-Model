from django.shortcuts import render
from django.views.generic import ListView
from .models import Category, Brand, Warranty, Seller, Product

# Class based (list-view) views.
class ProductListView(ListView):
    """
    This function is used for a ListView of all the products and 
    Display a paginated list of products with additional filtering options.
    """
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        """
        Get all the Category, Brand, Warranty & Seller data from database. 
        Add additional context data for rendering the template.
        -:return: string
        """
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['brands'] = Brand.objects.all()
        context['warranty'] = Warranty.objects.all()
        context['sellers'] = Seller.objects.all()
        return context
