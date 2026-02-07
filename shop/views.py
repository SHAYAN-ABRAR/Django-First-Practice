from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>SHOP Home Page!</h1>")
def Products(request):
    return HttpResponse("<h1>SHOP Products Page!</h1>") 
    
def product_list(request):
    return render(request, 'shop/product_list.html')
