import uuid

from django.db import models

# Create your models here.
from django.db.models import Model
from django.forms import forms


class Student(Model):
    id = models.CharField(max_length=15, blank=False, primary_key=True, help_text='''
                                                                Format: yycc-iii
                                                                yy - year
                                                                cc - class
                                                                iii - unique id''')


    def __str__(self):
        return str(self.id)


class Subject(Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_id = models.IntegerField(unique=False, default=uuid.uuid4)
    name = models.CharField(max_length=100, blank=False, unique=False)
    task_class = models.IntegerField(blank=False, unique=False, default=10)


    def __str__(self):
        return str(self.name) + " " + str(self.task_class)


class Result(Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student_reference = models.ForeignKey('Student', null=False, blank=False, on_delete=models.PROTECT)
    subject_reference = models.ForeignKey('Subject', null=False, blank=False, on_delete=models.PROTECT)
    score = models.CharField(max_length=200, blank=False, unique=False)


    def clean(self):
        same = Result.objects.\
            filter(student_reference=self.student_reference,
                   subject_reference=self.subject_reference)\
            .count()

        if same != 0:
            raise forms.ValidationError("Result with same parameters already exists")


    def __str__(self):
        student = str(self.student_reference)
        subject = str(self.subject_reference.name)
        return student + " " + subject + " результат:" + self.score + " класс работы: " + str(self.subject_reference.task_class)