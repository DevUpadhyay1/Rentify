from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from accounts.models import CustomeUser

class UserRegisterForm(UserCreationForm):
    # username = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Username","id":"username"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"email","id":"mail"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Password","id":"pass"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Confirm Password","id":"cpass"}))
    
    class Meta:
        model = CustomeUser
        fields = ['email']

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomeUser
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomeUser
        fields = ("email",)