from django import forms
from .models import Grade
from django.forms import PasswordInput
ROLE_CHOICES= [
    ('Student', 'Student'),
    ('Teacher', 'Teacher'),
    ('Parent', 'Parent'),
    ]
class registrationForm(forms.Form):
    name = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
  #  prefered_name= forms.CharField(max_length=50)
    address = forms.CharField(max_length=200)
    city = forms.CharField(max_length=50)
    state = forms.CharField(max_length=50)
    zipcode = forms.CharField(max_length=10)
    email = forms.EmailField(max_length=200)
    cell_phone = forms.CharField(max_length=50)
    role= forms.CharField(label='Role', widget=forms.Select(choices=ROLE_CHOICES))

class loginForm(forms.Form):
    Username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
	
class AttendancepForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ('attandance',)
class emailannouncement(forms.Form):
    mailtext = forms.CharField(widget=forms.Textarea)