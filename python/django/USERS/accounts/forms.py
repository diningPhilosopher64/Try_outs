from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class RegisterUser(UserCreationForm):
    first_name =  forms.CharField( max_length=50, required=True)
    last_name =  forms.CharField(max_length=50, required=True)   
    email = forms.EmailField( required=True)
    city = forms.CharField( max_length= 40, required=False)


    class Meta:
        model = User
        fields = ("first_name", "last_name","username", "email", "city","password1","password2")    

    def save(self, commit=True):
        user = super(RegisterUser, self).save(commit=False)

        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.city = self.cleaned_data['city']

        if commit:
            user.save()

        return user


