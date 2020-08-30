from django import forms
from .models import Bug

class BugReportForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ['bug_title', 'bug_description', 'screenshot']