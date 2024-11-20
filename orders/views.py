from django.shortcuts import render
from django.http import HttpResponse
from .models import Category
def signup_view(request):
    return render(request, 'signup.html')
def login_view(request):
    return render(request, 'login.html')
def home_view(request):
    categories = Category.objects.all()
    return render(request, 'home.html', {'categories': categories})
def bakeds_view(request):
    return render(request, 'bakeds.html')
def contact_view(request):
    return render(request, 'contact.html')
def drinks_view(request):
    return render(request, 'drinks.html')
def fastFood_view(request):
    return render(request, 'fastFood.html')
def sweets_view(request):
    return render(request, 'sweets.html')
def orders_view(request):
    return render(request, 'orders.html')
    
