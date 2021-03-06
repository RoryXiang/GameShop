from django.shortcuts import render
from .forms import Registerform, Loginform
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import User
from django.urls import reverse
import json


def index(request):
    user = request.session.get('user', False)

    return render(request, 'index.html', {'user': user})
# 显示页面


def registerView(request):
    user = request.session.get('user', False)
    print(user)
    if not user:
        return render(request, 'login.html')
    else :
        return HttpResponseRedirect('/index/')


def register(request):
    # 从 get 或者 post 请求中获取 next 参数值
    # get 请求中，next 通过 url 传递，即 /?next=value
    # post 请求中，next 通过表单传递，即 <input type="hidden" name="next" value="{{ next }}"/>
    redirect_to = request.POST.get('next', request.GET.get('next', ''))

    # 只有当请求为 POST 时，才表示用户提交了注册信息
    if request.method == 'POST':
        # request.POST 是一个类字典数据结构，记录了用户提交的注册信息
        # 这里提交的就是用户名（username）、密码（password）、确认密码、邮箱（email）
        # 用这些数据实例化一个用户注册表单
        form = Registerform(request.POST)

        # 验证数据的合法性
        print("---- ", form.is_valid)
        if form.is_valid():
            # 如果提交数据合法，调用表单的 save 方法将用户数据保存到数据库
            form = form.cleaned_data
            old_user = User.objects.filter(user_name=form.get("user_name")).first()
            if old_user:
                # flash('账号已存在', category='warning')
                # return redirect(url_for('user.register'))
                return HttpResponseRedirect(reverse('users:register'))
            user = User(user_name=form.get("user_name"),
                        password=form.get("password"),
                        yue=form.get("yue"))
            user.save()
            request.session["user_name"] = form.get("user_name")
            return HttpResponseRedirect(reverse('products:index'))
            # if redirect_to:
            #     return redirect(redirect_to)
            # else:
            #     return render(request, 'index.html')
    else:
        # 请求不是 POST，表明用户正在访问注册页面，展示一个空的注册表单给用户
        form = Registerform()
    # 渲染模板
    # 如果用户正在访问注册页面，则渲染的是一个空的注册表单
    # 如果用户通过表单提交注册信息，但是数据验证不合法，则渲染的是一个带有错误信息的表单
    # 将记录用户注册前页面的 redirect_to 传给模板，以维持 next 参数在整个注册流程中的传递
    return render(request, 'users/register.html', context={'form': form, 'next': redirect_to})


# 登录
def login(request):
    if request.method == "GET":
        form = Loginform()
        return render(request, 'users/login.html', context={'form': form})
    else:
        user_name = request.POST['user_name']
        password = request.POST['password']
        result = User.objects.get(user_name=user_name, password=password)

        if not result:
            return render(request, 'users/login.html')
        else:
            request.session['user_name'] = user_name
            return HttpResponseRedirect(reverse('products:index'))


# 注销
def logout(request):
    request.session.pop("user_name")
    return HttpResponseRedirect('users:login')


def yue(request):
    user_name = request.session.get("user_name")
    user = User.objects.filter(user_name=user_name).first()
    data = {"code": 200, "message": "购买成功", "yue": user.yue}
    return HttpResponse(json.dumps(data))

