from django.contrib import admin

# Register your models here.
from school_app.models import Student, OlympData


class StudentAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ('__str__',)


class OlympDataAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ('__str__',)


admin.site.register(Student, StudentAdmin)
admin.site.register(OlympData, OlympDataAdmin)
