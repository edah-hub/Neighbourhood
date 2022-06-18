from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# from registration.forms import RegistrationForm
from crispy_forms.helper import FormHelper


# class RegisterForm(RegistrationForm):
#     first_name = forms.CharField(max_length=255)
#     last_name = forms.CharField(max_length=255)
    
#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)
        
#     def __init__(self, *args, **kwargs):
#         super(RegistrationForm, self).__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         for fieldname in ['username', 'password1', 'password2']:
#             self.fields[fieldname].help_text = None
#         self.helper.form_show_labels = True 