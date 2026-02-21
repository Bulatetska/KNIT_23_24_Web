from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("<h1>Ласкаво просимо до нашого магазину!</h1>")
def category(request, category_n):
    return HttpResponse(f"<h1>Категорія: {category_n}</h1>")
def product(request, category_n, product_n):
    return HttpResponse(f"<h1>Товар: {product_n} у категорії {category_n}</h1>")
def sale(request):
    return HttpResponse("<h1>Акційні товари магазину</h1>")
# Create your views here.

