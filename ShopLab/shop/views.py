from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Ласкаво просимо до нашого магазину")
def category(request,category):
    return HttpResponse(f"Категорія:{category}")
def category_products(request,category,product):
    return HttpResponse(f"Товар: {product} у категорії {category}")
def sale(request):
    return HttpResponse(f"Акційні товари магазину")
def products(request):
    items = [
        {"name": "Ноутбук", "price": 1500, "stock": 0},
        {"name": "Смартфон", "price": 800, "stock": 15},
        {"name": "Навушники", "price": 200, "stock": 50},
    ]
    return render(request, "products.html", {"items": items})