from django.db import models
from django.contrib.auth.models import User

# Create models.
class Category(models.Model):
    """
    Defining this class is meant to store information related to Category.
    Name_of_the_Class: model class
    """
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        The __str__ method in a Django model is a special method that defines the human-readable representation of an object.  
        return: string
        """
        return self.name

class Brand(models.Model):
    """
    Defining this class is meant to store information related to Brand.
    Name_of_the_Class: model class
    """
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        The __str__ method in a Django model is a special method that defines the human-readable representation of an object.  
        return: string
        """
        return self.name

class Warranty(models.Model):
    """
    Defining this class is meant to store information related to Warenty.
    Name_of_the_Class: model class
    """
    duration = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        The __str__ method in a Django model is a special method that defines the human-readable representation of an object.  
        return: string
        """
        return self.duration

class Seller(models.Model):
    """
    Defining this class is meant to store information related to Sellers.
    Name_of_the_Class: model class
    """
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        The __str__ method in a Django model is a special method that defines the human-readable representation of an object.  
        return: string
        """
        return self.name

class Product(models.Model):
    """
    Defining this class is meant to store information related to Products.
    Name_of_the_Class: model class
    """
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    warranty = models.ForeignKey(Warranty, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(default='image/default.jpeg', 
                              upload_to='image',
                              blank=True,
                              null=True)
    created_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        The __str__ method in a Django model is a special method that defines the human-readable representation of an object.  
        return: string
        """
        return self.name
