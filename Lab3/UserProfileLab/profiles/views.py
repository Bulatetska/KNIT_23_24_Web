from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("Головна")
def about(request):
    return HttpResponse("Про сайт")
def contact(request):
    return HttpResponse("Контакти")
# Create your views here.
