from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from tript.models import TriptUser

class UserCreateForm(UserCreationForm):
    #password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model= get_user_model()
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Email'

##class TriptUserForm(forms.ModelForm):
##    class Meta():
##        model = TriptUser
 ##       fields = ('country','city')