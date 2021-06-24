from django import forms
from .models import UserRegistration
class Regtab(forms.ModelForm):
    class Meta:
        model=UserRegistration
        fields=['name','email','password','country']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
            'country':forms.TextInput(attrs={'class':'form-control'}),
        }
