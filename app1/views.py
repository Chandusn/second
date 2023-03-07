from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def app1_first(request):
    return HttpResponse('Hi App1 of First function')

def app1_second(request):
    return HttpResponse('App1 of Second Function')