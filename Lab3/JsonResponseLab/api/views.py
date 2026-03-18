from django.http import JsonResponse

def users_list(request):
    data = [
        {"name": "Ivan", "age": 25},
        {"name": "Maria", "age": 30}
    ]
    return JsonResponse(data, safe=False)
def user(request, name):
    data = {
        "name": name,
        "age": 25,
        "orders": ["Notebook", "smartfone"]
    }
    return JsonResponse(data)  