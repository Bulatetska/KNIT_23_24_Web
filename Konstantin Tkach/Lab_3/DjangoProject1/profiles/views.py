from django.http import HttpResponse, JsonResponse
import json

def index(request):
    if request.headers.get('Accept') == 'application/json':
        return JsonResponse({
            'message': 'Система профілів користувачів',
            'status': 'success'
        })
    return HttpResponse("Система профілів користувачів")

def user_list(request):
    users = ['Іван', 'Марія', 'Олег']
    if request.headers.get('Accept') == 'application/json':
        return JsonResponse({
            'users': users,
            'count': len(users)
        })
    return HttpResponse(f"Список користувачів: {', '.join(users)}")

def user_detail(request, username):
    if request.headers.get('Accept') == 'application/json':
        return JsonResponse({
            'username': username,
            'status': 'active',
            'profile': {
                'name': username,
                'joined': '2024-01-01'
            }
        })
    return HttpResponse(f"Користувач: {username}")

def user_orders(request, username):
    orders = ['Замовлення #1', 'Замовлення #2', 'Замовлення #3']
    if request.headers.get('Accept') == 'application/json':
        return JsonResponse({
            'username': username,
            'orders': orders,
            'total_orders': len(orders)
        })
    return HttpResponse(f"Замовлення користувача: {username}")
