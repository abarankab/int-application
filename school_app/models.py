import uuid

from django.db import models

# Create your models here.
from django.db.models import Model
from django.forms import forms


class Student(Model):
    id = models.CharField(max_length=15, blank=False, primary_key=True)


    def __str__(self):
        return str(self.id)


class OlympData(Model):
    student_reference = models.ForeignKey('Student', null=False, blank=False, on_delete=models.PROTECT)
    subject = models.CharField(max_length=100, blank=False)
    login = models.CharField(max_length=100, blank=False)
    date = models.CharField(max_length=100, blank=False)


    def __str__(self):
        return str(self.student_reference.id) + " " +\
               str(self.subject) + " " +\
               str(self.login) + " " +\
               str(self.date)
