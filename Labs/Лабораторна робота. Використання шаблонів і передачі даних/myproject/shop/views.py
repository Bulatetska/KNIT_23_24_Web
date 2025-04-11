from django.shortcuts import render

def products(request):
    items = [
        {"name": "Ноутбук", "price": 1500, "stock": 10},
        {"name": "Смартфон", "price": 800, "stock": 15},
        {"name": "Навушники", "price": 200, "stock": 0},  # Приклад товару, якого немає в наявності
    ]
    return render(request, "products.html", {"items": items})