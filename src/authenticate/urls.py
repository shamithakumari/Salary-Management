from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    # path('', views.home, name="home"),
    path('signup', views.signup, name="signup"),
    path('', views.signin, name="signin"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
    path('index', views.index, name="index"),
    path('a_index', views.accountant_index, name="a_index"),
]