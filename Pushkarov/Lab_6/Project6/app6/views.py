from django.shortcuts import render
from .forms import UserForm
from django.http import HttpResponse
def index(request):
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            return HttpResponse(f"<h2>Form valid</h2>")

        else:
            message = "Form is not valid"
            return render(request, "index.html", {"form": userform, "message": message})
    else:
        userform = UserForm()
        return render(request, "index.html", {"form": userform})
