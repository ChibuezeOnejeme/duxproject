from django import forms
from .models import Searched_data
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ip_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ip_form, self).__init__(*args, **kwargs)
        self.fields['ip'].widget.attrs['placeholder'] = 'search ip' # this adds place holder to form
    class Meta:
        model = Searched_data
        fields = ['ip'] # this acesses all the field in searched_data model
	

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user