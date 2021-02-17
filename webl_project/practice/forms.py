from django import forms

from .models import Submissions

class SubmissionsForms(forms.ModelForm):
    class Meta:
        model = Submissions
        fields = ('title', 'code')