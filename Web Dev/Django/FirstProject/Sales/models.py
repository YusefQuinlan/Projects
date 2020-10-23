from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    trustworthy = models.BooleanField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Orders(models.Model):
    STATUS = (
        ('Paid For','Paid For'),
        ('Debt Due','Debt Due'),
        )
    Number = models.CharField(max_length=200,null=True)
    Customer = models.ForeignKey(Customer, on_delete=models.SET("Unknown"))
    Order_val = models.FloatField(null=True)
    Products_Sold = models.ManyToManyField(Product)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    
    def __str__(self):
        return self.Number

class Lead(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    staff_name = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.name
    