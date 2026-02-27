from django.http import HttpResponse
# Create your views here.
def index(request):
 return HttpResponse("Ласкаво просимо до нашого магазину")
def sale(request):
 return HttpResponse("Акційні товари магазину")
def category(request, category):
 return HttpResponse(f"Категорія: {category}")
def product_name(request, category, product):
    return HttpResponse(f"Товар: {product} у категорії {category}")
