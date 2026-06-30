from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        # We only need the user to type a title. The 'completed' status defaults to False!
        fields = ['title']