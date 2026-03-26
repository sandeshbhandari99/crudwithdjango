from django import forms
from .models import Result

class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = '__all__'
        widgets = {
            'student_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter student name',
            }),
            'roll_number': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter roll number',
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter subject name',
            }),
            'marks': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0 - 100',
                'min': 0,
                'max': 100,
            }),
            'grade': forms.Select(attrs={
                'class': 'form-control',
            }),
        }

    def clean_marks(self):
        marks = self.cleaned_data['marks']
        if marks > 100 or marks < 0:
            raise forms.ValidationError("Marks must be between 0 and 100.")
        return marks
