from django.shortcuts import render
from django.http import HttpResponse
from .models import*
 
# Create your views here.
#Home page
def Home(request):
    return render(request, 'Sales/Index.html')

"""Sales page that contains all the sales details via Orders.objects.all()
  query, missing the Customers information as not sure how to deal with many
  to many relations in Django yet.
"""

def Sales(request):
    Sales = Orders.objects.all()
    return render(request, 'Sales/sales.html',{'Orders':Sales})

"""Products page returns all products and their details via Product.object.all()
 query"""
 
def Products(request):
    Products = Product.objects.all()
    return render(request, 'Sales/products.html',{'Products':Products})

"""Customers page returns all products and their details via Product.object.all()
 query"""
 
def Customers(request):
    Customers = Customer.objects.all()
    return render(request, 'Sales/Customers.html',{'Customers':Customers})

"""Leads page returns all products and their details via Product.object.all()
 query"""
 
def Leads(request):
    Leads = Lead.objects.all()
    return render(request, 'Sales/leads.html',{'Leads':Leads})

"""Dynamic page return that returns a specific order/sale and its details
   as indicated by the id of the order in the url (see urls.py - Sales)
"""

def Sales2(request, sale_id):
    Sale = Orders.objects.get(id=sale_id)
    return render(request,'Sales/Salesheet.html',{'Sale':Sale} )

"""Dynamic page return that returns a specific Product and its details
   as indicated by the id of the Product in the url (see urls.py - Sales)
"""

def Products2(request, Product_id):
    Producta = Product.objects.get(id=Product_id)
    return render(request,'Sales/Productsheet.html',{'Product':Producta})

"""Dynamic page return that returns a specific Customer and its details
   as indicated by the id of the customer in the url (see urls.py - Sales)
"""

def Customers2(request, Customer_id):
    Customar = Customer.objects.get(id=Customer_id)
    return render(request, 'Sales/Customersheet.html', {'Customer':Customar})

"""Dynamic page return that returns a specific Lead and its details
   as indicated by the id of the Lead in the url (see urls.py - Sales)
"""

def Leads2(request, Lead_id):
    Leead = Lead.objects.get(id=Lead_id)
    return render(request, 'Sales/Leadsheet.html', {'Lead':Leead})