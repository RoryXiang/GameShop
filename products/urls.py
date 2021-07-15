from django.conf.urls import url

from . import views

app_name = 'products'
urlpatterns = [
    url(r'^buy/', views.buy, name='buy'),
    url(r'^index/', views.index, name='index'),
]