from .models import Organization, Student
from django import forms


class OrgRegisterForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

        css = {'class': "form-control", 'size': "35", 'maxlength': "60"}
        widgets = {
            'username': forms.TextInput(attrs=css),
            'password': forms.PasswordInput(attrs=css),
            'phone': forms.TextInput(attrs=css),
            'email': forms.EmailInput(attrs=css),
            'logo': forms.FileInput(attrs=css),
        }


class StuRegisterForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

        # css = {'class': "", 'size': "35", 'maxlength': "60"}
        widgets = {
            'username': forms.TextInput(attrs={'placeholder':'username', 'class': "form-control", 'size': "35", 'maxlength': "60"}),
            'password': forms.PasswordInput(attrs={'placeholder':'password', 'class': "form-control", 'size': "35", 'maxlength': "60"}),
            'school': forms.TextInput(attrs={'placeholder':'school', 'class': "form-control", 'size': "35", 'maxlength': "60"}),
            'email': forms.EmailInput(attrs={'placeholder':'email', 'class': "form-control", 'size': "35", 'maxlength': "60"}),
            'phone': forms.TextInput(attrs={'placeholder':'phone', 'class': "form-control", 'size': "35", 'maxlength': "60"}),
        }

class StuLoginForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['username', 'password']

        # css = {'class': "", 'size': "35", 'maxlength': "60"}
        widgets = {
            'username': forms.TextInput(attrs={'placeholder':'username', 'class': "form-control", 'size': "35", 'maxlength': "60"}),
            'password': forms.PasswordInput(attrs={'placeholder':'password', 'class': "form-control", 'size': "35", 'maxlength': "60"}),
        }


class OrgLoginForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['username', 'password']

        # css = {'class': "", 'size': "35", 'maxlength': "60"}
        widgets = {
            'username': forms.TextInput(attrs={'placeholder':'username', 'class': "form-control", 'size': "35", 'maxlength': "60"}),
            'password': forms.PasswordInput(attrs={'placeholder':'password', 'class': "form-control", 'size': "35", 'maxlength': "60"}),
        }
