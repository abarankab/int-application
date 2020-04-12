from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_protect

from school_app.models import Student, OlympData
from django.contrib import messages


class IdPendingView(View):
    def get(self, request):
        return render(request, "main.html")


def olymp_key(olymp):
    month_order = {
        "апреля": 0,
        "мая": 4
    }

    day, month = olymp["date"].split(" ")
    return (month_order[month], day)


class GetOlympView(View):

    @method_decorator(csrf_protect)
    def post(self, request):
        id = request.POST.get("id", "")

        if id.strip() != "" and Student.objects.filter(id=id).count() != 0:
            olymp_data_raw = OlympData.objects.filter(student_reference=id).order_by("date")
            olymp_data = []

            for olymp in olymp_data_raw:
                olymp_data.append({
                    "subject": olymp.subject,
                    "date": olymp.date,
                    "login": olymp.login,
                })

            olymp_data.sort(key=olymp_key)

            return render(request, "results.html", {"olymp_data": olymp_data, "id": id})

        elif id.strip() != "":
            messages.error(request, "Ученика с таким ID нет")
            return redirect("/")

        else:
            messages.error(request, "Вы случайно ввели пустой ID")
            return redirect("/")
