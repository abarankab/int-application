import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "school.settings")
django.setup()

from school_app.models import Result, Subject, Student

Result.objects.all().delete()
Subject.objects.all().delete()
Student.objects.all().delete()