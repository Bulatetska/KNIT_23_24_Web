from django.http import HttpResponse

def home(request):
    return HttpResponse("Ласкаво просимо до нашого магазину")

def category_detail(request, category):
    return HttpResponse(f"Категорія: {category}")

def product_detail(request, category, product):
    return HttpResponse(f"Товар: {product} у категорії {category}")

def sale(request):
    return HttpResponse("Акційні товари магазину")