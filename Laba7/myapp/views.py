from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Привет!')

def about(request):
    return HttpResponse('Стриница')
