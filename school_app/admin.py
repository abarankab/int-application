from django.contrib import admin

# Register your models here.
from school_app.models import Student, Subject, Result


class IntAdmin(admin.ModelAdmin):

    admin.site.register(Student)
    admin.site.register(Subject)
    admin.site.register(Result)

    list_display = ('Student', 'Subject', 'Result')

    #TODO search fields