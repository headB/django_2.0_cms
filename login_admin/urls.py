from django.conf.urls import url
from django.urls import path
from  login_admin import views

urlpatterns = [

    path('index',views.register),
    path('index/<str:name>',views.register_other)

]