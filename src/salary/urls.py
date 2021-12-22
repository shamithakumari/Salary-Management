from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.details, name="details"),
    path('accountants',views.accountants, name="accountants"),
    path('accountants/<int:userid>',views.accountantind, name="accountants")
    # path('/history',views.history, name="history")
]