from django import forms
from .models import *



class RegisterForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'required': 'true' ,'placeholder': 'username'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'firstname'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'lastname'}),
            'email': forms.TextInput(attrs={'class': 'form-control','placeholder': 'email'}),
            'password': forms.TextInput(attrs={'class': 'form-control', 'required': 'true','placeholder': 'pasword'}),
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date of Birth', 'type': 'date'}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control', 'required': 'true'}),
        }


class CSVUploadForm(forms.Form):
    csv_file = forms.FileField()