from django.contrib.auth.forms import UserCreationForm

from .models import User


# class RegisterForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = User
#         fields = ("user_name", "yue")

from django import forms


class Registerform(forms.Form):
    user_name = forms.CharField(min_length=8, label="用户名")
    password = forms.CharField(min_length=6, label="密码")
    yue = forms.IntegerField()


class Loginform(forms.Form):
    user_name = forms.CharField(min_length=8, label="用户名")
    password = forms.CharField(min_length=6, label="密码")


# from pydantic import BaseModel

# class RegisterForm(BaseModel):
#     user_name: str,
#     password: str,
#     yue: float,