from django import forms
from school_app.models import Student

class IdForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('id',)