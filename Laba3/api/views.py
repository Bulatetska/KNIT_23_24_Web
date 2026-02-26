from django.http import JsonResponse

def api_user_list(request):
    data = [{"name": "Іван", "age": 25}, {"name": "Марія", "age": 30}]
    return JsonResponse(data, safe=False)

def api_user_detail(request, name):
    data = {"name": name, "age": 25, "orders": ["Ноутбук", "Смартфон"]}
    return JsonResponse(data)