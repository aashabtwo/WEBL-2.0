from django import forms

from .models import AssignmentSubmissions

class AssignmentSubmissionsForm(forms.ModelForm):
    class Meta:
        model = AssignmentSubmissions
        fields = ('code',)