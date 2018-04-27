from django.shortcuts import render
from django.shortcuts import HttpResponse,redirect
# Create your views here.
from login_admin import *
##这里是控制器

##定义一个注册
def register(request):
    #print(args)
    return render(request,'login_admin/index.html')

##定义一个通过的控制器,就是加入用户前面匹配到一些主要入口.

def register_other(request,name):
    print(request.GET)
    print(request.POST)
    #print(args)
    print(name)

    return render(request,'login_admin/index.html')