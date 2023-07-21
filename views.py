from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def fun(request):
    return HttpResponse("Fun  is outside not  in class")
def happy(request):
    return HttpResponse("<h1><marquee>Always be happy and be cool</h1></marquee>")