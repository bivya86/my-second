from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def dia(request):
    return HttpResponse('it is a nice movie')