from django.shortcuts import render, redirect
from .models import Student

def home(request):

    if request.method == "POST":

        # ➕ ДОДАТИ
        if "add" in request.POST:
            Student.objects.create(
                name=request.POST["name"],
                year=int(request.POST["year"]),
                ticket=request.POST["ticket"]
            )

        # 🔄 ОНОВИТИ
        elif "update" in request.POST:
            try:
                s = Student.objects.get(ticket=request.POST["ticket"])
                s.year = int(request.POST["year"])
                s.save()
            except:
                pass

        # ❌ ВИДАЛИТИ ОДНОГО
        elif "delete_one" in request.POST:
            Student.objects.filter(ticket=request.POST["ticket"]).delete()

        return redirect("/")

    students = Student.objects.all().order_by("-year")
    return render(request, "index.html", {"students": students})