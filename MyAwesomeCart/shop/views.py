from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact
from math import ceil

# Create your views here.

def index(request):
    # products = Product.objects.all()
    # print(products)

    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))
    # params = {'no_of_slides': nSlides, 'range': range(1, nSlides), 'product': products}

    allProds = []
    catprods = Product.objects.values('categories', 'id')
    # item comprihension
    cats = {item['categories'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(categories=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    # allProds = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]
    params ={'allProds':allProds}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    if request.method == "POST":

        name = request.POST.get('name', '')
        email =request.POST.get('email', '')
        phone =request.POST.get('phone', '')
        desc = request.POST.get('message', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'shop/contact.html')

def tracker(request):
    return render(request, 'shop/tracker.html')

def search(request):
    return render(request, 'shop/search.html')

def productView(request, myid):
    # Fetch the product using the id
    product = Product.objects.filter(id=myid)
    print(product)
    return render(request, 'shop/prodView.html', {'product': product[0]})

def checkout(request):
    return render(request, 'shop/checkout.html')



