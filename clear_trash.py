import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "school.settings")
django.setup()

from school_app.models import Student, OlympData

OlympData.objects.all().delete()
Student.objects.all().delete()
