from django.shortcuts import render
# from .forms import Registerform, Loginform
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import Products
from django.core import serializers
import json


# def list(request):
#     products = Products.objects.filter()
#     for p in products:
#         print(p.name, p.price)
#     print(products)


def buy(request, product_id):
    pass


def index(request):
    form = []
    if request.session.get("user_name"):
        products = Products.objects.filter()
        result_serialize = serializers.serialize('json',products)
        form = json.loads(result_serialize) # 对序列化之后的str类型数据进行转化为json对象
        form = [x["fields"] for x in form]
    print(form)
    return render(request, 'index.html', context={'products': form})