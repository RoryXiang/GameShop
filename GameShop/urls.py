"""GameShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
from django.conf.urls import url, include
from django.contrib import admin

from User import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 别忘记在顶部引入 include 函数
    url(r'^User/', include('User.urls')),
    url(r'^User/', include('django.contrib.auth.urls')),
    url(r'^$', views.index, name='index')
]