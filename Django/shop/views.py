from django.shortcuts import render

def products(request):
    items = [
        {"name": "Ноутбук", "price": 1500, "stock": 10},
        {"name": "Смартфон", "price": 800, "stock": 15},
        {"name": "Навушники", "price": 200, "stock": 50},
    ]

    return render(request, "products.html", {"items": items})

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")
