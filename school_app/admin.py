from django.contrib import admin

# Register your models here.
from school_app.models import Student, Subject, Result


class ResultAdmin(admin.ModelAdmin):
    list_display = ('student_reference', 'subject_reference')
    search_fields = (
        'student_reference__id',
    )

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('__str__',)

admin.site.register(Result, ResultAdmin)
admin.site.register(Subject, SubjectAdmin)