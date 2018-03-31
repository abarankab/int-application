from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_protect

from school_app.models import Result, Subject
from django.contrib import messages


class IdPendingView(View):
    def get(self, request):
        return render(request, 'main.html')


class GetResultsView(View):
    @method_decorator(csrf_protect)
    def post(self, request):
        id = request.POST.get('id', '')

        if id.strip() != '' and Result.objects.filter(student_reference=id).count() != 0:
            
            results_raw = Result.objects.filter(student_reference=id).order_by('subject_reference')
            results = {'results' : []}

            for result in results_raw:
                score = result.score
                name = result.subject_reference.name

                results['results'].append({
                                'name' : name,
                                'score' : score,
                                })

            return render(request, 'results.html', results)

        elif id.strip() != '':
            messages.error(request, "Поступающего с таким ID нет")
            return redirect('/')

        else:
            messages.error(request, "Вы случайно ввели пустой ID")
            return redirect('/')