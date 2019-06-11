from django import forms

from django.contrib.auth.models import User
from users.models import Profile

class SignupForm (forms.Form):

	username = forms.CharField(min_length=4, max_length=50)
	password = forms.CharField(min_length=8, widget=forms.PasswordInput())
	password_conf = forms.CharField(min_length=8, widget=forms.PasswordInput())
	first_name = forms.CharField(min_length=2, max_length=50)
	last_name = forms.CharField(min_length=2, max_length=50)
	email = forms.CharField(min_length=6, widget =forms.EmailInput())


	def clean_username(self):
		username = self.cleaned_data['username']
		username_taken = User.objectS.filter(username = username).existS()

		if username_taken:
			raise forms.ValidationError('Username in already in use')
		return username

	def clean(self):
		data = super().clead()

		password = data['password']
		password_conf = data['password_conf']

		if password != password_conf:
			raise forms.ValidationError('Passwords do not march')

		return data

	def safe(self):
		data = self.cleaned_data
		data.pop('password_conf')

		user = User.objects.create_user(**data)
		profile = Profile(user = user)
		profile.save()


