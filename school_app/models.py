from django.db import models

# Create your models here.
from django.db.models import Model


class Student(Model):
    id = models.CharField(max_length=15, blank=False, primary_key=True, help_text='''
                                                                Format: yycc-iiii
                                                                yy - year
                                                                cc - class
                                                                iiii - unique id''')


    def __str__(self):
        return str(self.id)


class Subject(Model):
    id = models.IntegerField(blank=False, primary_key=True)
    name = models.CharField(max_length=100, blank=False, unique=False)
    task_class = models.IntegerField(blank=False, unique=False)
    #max_score = models.IntegerField(blank=False, unique=False) TODO


    def __str__(self):
        return str(self.name)


class Result(Model):
    student_id = models.ForeignKey('Student', on_delete=models.PROTECT)
    subject_id = models.ForeignKey('Subject', on_delete=models.PROTECT)
    score = models.CharField(max_length=200, blank=False, unique=False)

    def __str__(self):
        student = str(self.student_id)
        subject = str(self.subject_id.name)
        return student + " " + subject