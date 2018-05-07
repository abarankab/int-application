import openpyxl as op
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "school.settings")
django.setup()

from school_app.models import Subject, Student, Result

print("Какой worksheet парсить?")
ind = int(input()) - 1

wb = op.load_workbook("table.xlsx")
ws = wb.worksheets[ind]
grade = int(wb.sheetnames[ind][1])

raw_pattern = ws['C1':'O1']
pattern = []
for cell in raw_pattern[0]:
    if cell.value == None:
        break
    pattern.append(cell.value)

people = []

for current_subject in pattern:
    exists = Subject.objects.filter(name=current_subject, task_class=grade).count() == 1
    if not exists:
        new_subject = Subject(name=current_subject, task_class=grade, order_id=0)
        new_subject.save()

print(grade)
print(pattern)

for i in range(1, 10000):
    A = 'A' + str(i + 1)
    C = 'C' + str(i + 1)
    O = 'O' + str(i + 1)

    if ws[A].value == None:
        break

    raw_row = ws[C:O]
    current_row = []
    for cell in raw_row[0]:
        current_row.append(str(cell.value))
    current_row = current_row[:len(pattern)]
    current_id = str(ws[A].value)
    people.append([current_id, current_row])

for person in people:
    if Student.objects.filter(id=person[0]).count() == 0:
        new_student = Student(id=person[0])
        new_student.save()
    else:
        print("Collision, {}".format(person[0]))

    for i in range(len(pattern)):
        if person[1][i] != "None":
            current_student = Student.objects.get(id=person[0])
            current_subject = Subject.objects.get(name=pattern[i], task_class=grade)

            new_result = Result(student_reference=current_student,
                                subject_reference=current_subject,
                                score=person[1][i])

            new_result.save()


exit(0)