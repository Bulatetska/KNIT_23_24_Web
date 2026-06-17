from django.http import HttpResponse

def index(request):
    return HttpResponse("Ласкаво просимо до нашого магазину")

def category(request, category):
    return HttpResponse(f"Категорія: {category}")

def product(request, category, product):
    return HttpResponse(f"Товар: {product} у категорії {category}")

def sale(request):
    return HttpResponse("Акційні товари магазину")