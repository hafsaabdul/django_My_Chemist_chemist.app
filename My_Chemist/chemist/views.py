from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'chemist/index.html')

def products(request):
    return render(request,'chemist/products.html')

def search(request):
    pass

def about(request):
    return render(request, 'chemist/about-us.html')

def contact(request):
    return render(request, 'chemist/contact.html')