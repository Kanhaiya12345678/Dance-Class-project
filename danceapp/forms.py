from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'password', 'username')

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ('classname', 'name', 'gender', 'mobile', 'email', 'registernumber', 'message')

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ('classname', 'image', 'description', 'cost')

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('classname', 'teachername', 'teacherimage', 'mobile', 'email')

