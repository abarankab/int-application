from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_protect

from school_app.models import Result, Subject, Student
from django.contrib import messages

class IdPendingView(View):
    def get(self, request):
        return render(request, 'main.html')


class GetResultsView(View):
    def convert(self, value):
        try:
            return int(value)
        except ValueError:
            return float(value)


    @method_decorator(csrf_protect)
    def post(self, request):
        id = request.POST.get('id', '')

        import logging
        logging.warning(id)
        logging.warning(Student.objects.filter(id=id).count())

        if id.strip() != '' and Student.objects.filter(id=id).count() != 0:

            grade = int(str(id)[2:4])
            
            results_raw = Result.objects.filter(student_reference=id).order_by(
                ('subject_reference__order_id'))

            payload = {'results' : []}
            parts = []
            scores = []
            sum_of_best = 0
            max_sum = 0

            for result in results_raw:
                score = result.score
                name = result.subject_reference.name

                payload['results'].append({
                                'name': name,
                                'score': score,
                                'highlighted': False,
                                })

                if grade != 10:
                    payload['results'][-1]['score'] = self.convert(payload['results'][-1]['score'])

                if grade != 10 and name != "Тест по математике" and name != "Межпредметный тест":
                    scores.append((self.convert(score), name,))
                elif grade != 10:
                    payload['results'][-1]['highlighted'] = True
                    sum_of_best += self.convert(score)
                    max_sum += 20
                    parts.append(str(score))

            scores.sort(key=lambda x: -x[0])

            for i in range(len(payload['results'])):

                if grade != 10 and\
                        (payload['results'][i]['name'] == scores[0][1] or payload['results'][i]['name'] == scores[1][1]):

                    payload['results'][i]['highlighted'] = True
                    sum_of_best += payload['results'][i]['score']
                    max_sum += 20
                    parts.append(str(payload['results'][i]['score']))

            from logging import warning

            payload['mark'] = "Итог: " + " + ".join(parts) + " = " + str(sum_of_best) + " из " + str(max_sum)
            payload['id'] = id
            payload['grade'] = 10

            return render(request, 'results.html', payload)

        elif id.strip() != '':
            messages.error(request, "Поступающего с таким ID нет")
            return redirect('/')

        else:
            messages.error(request, "Вы случайно ввели пустой ID")
            return redirect('/')