from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def products(request):
    return render(request, 'products.html')

def contact_us(request):
    return render(request, 'contact_us.html')

def product1(request):
    return render(request, 'product1.html')

def product2(request):
    return render(request, 'product2.html')

def product3(request):
    return render(request, 'product3.html')

def product4(request):
    return render(request, 'product4.html')

def product5(request):
    return render(request, 'product5.html')

def product6(request):
    return render(request, 'product6.html')

def services(request):
    return render(request, 'services.html')

def sold_out(request):
    return render(request, 'sold_out.html')

def sell(request):
    return render(request, 'sell.html')