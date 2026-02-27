from django.http import HttpResponse
# Create your views here.
def index(request):
 return HttpResponse("Система профілів користувачів")
def users(request):
 return HttpResponse("Список користувачів: Іван, Марія, Олег")
def user_name(request, username):
 return HttpResponse(f"Користувач: {username}")
def orders(request, username):
 return HttpResponse(f"Замовлення користувача: {username}")