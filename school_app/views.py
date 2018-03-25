from django.shortcuts import render, redirect

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_protect

from school_app.forms import IdForm
from school_app.models import Result, Subject
from logging import error


class IdPendingView(View):
    def get(self, request):
        return render(request, 'main.html')


class GetResultsView(View):
    @method_decorator(csrf_protect)
    def post(self, request):
        id = request.POST.get('id', '')

        if id.strip() != '' and Result.objects.filter(student_id=id).count() != 0:
            
            results_raw = Result.objects.filter(student_id=id).order_by('subject_id')
            results = {'results' : []}

            for result in results_raw:
                score = result.score
                name = result.subject_id.name

                results['results'].append({
                                'name' : name,
                                'score' : score,
                                })

            return render(request, 'results.html', results)

        else:
            return redirect('/')