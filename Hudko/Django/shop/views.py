from django.shortcuts import render

def products(request):
    items = [
        {"name": "Ноутбук", "price": 1500, "stock": 10},
        {"name": "Смартфон", "price": 800, "stock": 15},
        {"name": "Навушники", "price": 200, "stock": 50},
        {"name": "Планшет", "price": 1000, "stock": 0},
        {"name": "Смарт-годинник", "price": 340, "stock": 15},
        {"name": "Повербанк", "price": 400, "stock": 50},
    ]
    return render(request, "products.html", {"items": items})