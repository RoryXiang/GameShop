from django.shortcuts import render
# from .forms import Registerform, Loginform
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import Products


def list(request):
    products = Products.objects.filter()
    for p in products:
        print(p.name, p.price)
    print(products)


def buy(request, product_id):
    pass


def index(request):
    form = []
    return render(request, 'index.html', context={'form': form})