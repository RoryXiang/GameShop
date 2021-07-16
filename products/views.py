from django.shortcuts import render
# from .forms import Registerform, Loginform
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import Products
from django.core import serializers
import json
from .models import Products
from User.models import User


def buy(request):
    product_name = request.GET.get("product_name")
    print(product_name)
    user_name = request.session.get("user_name")
    user = User.objects.filter(user_name=user_name).first()
    product = Products.objects.filter(name=product_name).first()
    if int(user.yue) < int(product.price):
        return {"code": 444, "message": "购买失败"}
    user.yue -= product.price
    user.save()
    data = {"code": 200, "message": "购买成功", "yue": user.yue - product.price}
    return HttpResponse(json.dumps(data))


def index(request):
    form = []
    if request.session.get("user_name"):
        products = Products.objects.filter()
        result_serialize = serializers.serialize('json', products)
        form = json.loads(result_serialize)  # 对序列化之后的str类型数据进行转化为json对象
        form = [x["fields"] for x in form]
    print(form)
    return render(request, 'index.html', context={'products': form})
