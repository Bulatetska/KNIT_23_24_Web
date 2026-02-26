from django.http import HttpResponse

def shop_home(request): return HttpResponse("Ласкаво просимо до нашого магазину")
def category_view(request, category): return HttpResponse(f"Категорія: {category}")
def product_view(request, category, product): return HttpResponse(f"Товар: {product} у категорії {category}")
def sale_view(request): return HttpResponse("Акційні товари магазину")