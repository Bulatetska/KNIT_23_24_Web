from django.http import JsonResponse

json = [
{"name": "Іван", "age": 25},
{"name": "Марія", "age": 30}
]


def users(request):
    return JsonResponse(json, safe=False, json_dumps_params={'ensure_ascii': False})

def name(request, name):
    user = next((item for item in json if item["name"] == name), None)
    if user:
        return JsonResponse(user, safe=False, json_dumps_params={'ensure_ascii': False})
    else:
        return JsonResponse({"error": "Користувача не знайдено"}, status=404)
