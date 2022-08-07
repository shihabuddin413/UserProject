
from logging import PlaceHolder
from django import forms
# from django.forms import ModelForm
from .models import JobApplication


class JobApplicationForm(forms.ModelForm):

    class Meta:
        model = JobApplication
        fields = ('job_title', 'job_description', 'job_vacancy', 'job_location', 'working_days', 'working_hours', 'job_type',
                  'job_industry', 'salary_expectation', 'job_pay_rate_type', 'required_job_experince', 'require_job_skill')

        widgets = {
            'job_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'job title '}),
            'job_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'job description here ... '}),
            'job_vacancy': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Number of vacancey'}),
            'job_location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter google map url... '}),
            'working_days': forms.Select(attrs={'class': 'form-select'}),
            'working_hours': forms.Select(attrs={'class': 'form-select'}),
            'job_type': forms.Select(attrs={'class': 'form-select'}),
            'job_industry': forms.Select(attrs={'class': 'form-select'}),
            'salary_expectation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Salary expectations is USD'}),
            'job_pay_rate_type': forms.Select(attrs={'class': 'form-select'}),
            'required_job_experince': forms.Select(attrs={'class': 'form-select'}),
            'require_job_skill': forms.Select(attrs={'class': 'form-select'}),
        }
