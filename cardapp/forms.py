from django import forms
from .models import User
class formsdata(forms.ModelForm):
    class Meta:
        model=User
        fields = ('id','name','email','password')
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please Enter Your Valid Name'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Please Enter Your Valid Email Address'}),
            'password':forms.PasswordInput(render_value=True, attrs={'class':'form-control','placeholder':'Please Enter Strong Password'})
            
        }