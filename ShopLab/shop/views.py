from django.http import HttpResponse

category_and_products = {
    "Vegetables" : ["Tomato", "Potato", "Carrot"],
    "Electronic" : ["Phone", "Generator", "Laptop"],
}


def index(request):
    return HttpResponse("Ласкаво просимо до нашого магазину.")

def shop_category(request, category):
    if category in category_and_products:
        return HttpResponse("Категорія: " + category)
    return HttpResponse("Категорії " + category + " неіснує")

def shop_product(request, category, product):
    if category not in category_and_products:
        return HttpResponse("Категорії " + category + " неіснує")
    if product not in category_and_products[category]:
        return HttpResponse("Товару " + category + " в категорії " + category + " неіснує")
    return HttpResponse(f"Товар: {product} у категорії {category}")

def sale(request):
    return HttpResponse("Акційні товари магазину")