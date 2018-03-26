from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_protect

from school_app.models import Result, Subject


class IdPendingView(View):
    def get(self, request, error):
        if error == "incorrect":
            return render(request, 'main.html', {'errors' : ['1']})
        elif error == "":
            return render(request, 'main.html', {'errors' : []})
        else:
            return HttpResponseNotFound()


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

        else:
            return redirect('/incorrect')