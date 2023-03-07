from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app2_first(request):
    return HttpResponse('App2 of First Function')

def app2_second(request):
    return HttpResponse('App2 of second Function')