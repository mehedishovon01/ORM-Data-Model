from django.shortcuts import render
from django.views.generic import ListView
from .models import Category, Brand, Warranty, Seller, Product

# Class based (list-view) views.
class ProductListView(ListView):
    """
    Display a paginated list of products with additional filtering options.
    """
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        """
        Add additional context data for rendering the template.
        """
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['brands'] = Brand.objects.all()
        context['warranty'] = Warranty.objects.all()
        context['sellers'] = Seller.objects.all()
        return context
