from django.http import HttpResponse

def index(request):
    return HttpResponse("Ласкаво просимо до нашого магазину")

def sale(request):
    return HttpResponse("Акційні товари магазину")

def category_view(request, category):
    return HttpResponse(f"Категорія: {category}")

def product_view(request, category, product):
    return HttpResponse(f"Товар: {product} у категорії {category}")
