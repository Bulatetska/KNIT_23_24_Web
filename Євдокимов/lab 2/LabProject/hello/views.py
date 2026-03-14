from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse #Імпортує клас для відправки тексту в браузер
def index(request): #створює фуркцію подання (view)
    return HttpResponse("Hello, World!")#повертаємо текст хелов ворлд