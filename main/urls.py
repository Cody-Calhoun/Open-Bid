from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('con_home', views.con_home),
    path('contractor_reg_login', views.con_reg_form),
    path('con_register', views.con_register),
    path('con_login', views.con_login),
    path('customer_reg_login', views.cus_reg_form),
    path('cus_register', views.cus_register),
    path('cus_home', views.cus_home),
    path('cus_login', views.cus_login),
    path('logout', views.logout),
    path('specialty_add', views.specialty_add),
    path('cus_view_proj/<int:id>', views.project_info),
    path('cus_view_bid/<int:id>', views.cus_view_bid),

]

