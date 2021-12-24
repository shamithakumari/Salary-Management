from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.details, name="details"),

    path('accountants/',views.accountants, name="accountants"),
    path('accountants/<int:userid>',views.accountants_with_userid, name="accountants"),
    
    path('history/',views.history, name="history"),
    path('history/<int:userid>',views.history_with_userid, name="history"),
    # path('/history',views.history, name="history")

    path('history/update/<int:slipno>',views.salary_slip_update,name="salary_slip_update")

]