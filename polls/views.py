from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello,GK")

def indexchinmay(request):
    return HttpResponse("Hello,CHINMAY")

def gaurav(request):
    return HttpResponse("Hello,gaurav")
