from django.http import HttpResponse

def index(request):
    return HttpResponse("Ласкаво просимо до нашого магазину")

def sale(request):
    return HttpResponse("Акційні товари магазину")

def category(request,category):
 return HttpResponse(f"Категорія: {category}")

def product_name(request,category,product_name):
 return HttpResponse(f"Товар: {product_name} у категорії {category}")  