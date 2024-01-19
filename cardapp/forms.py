from django import forms
from .models import User
class StudentForms(forms.ModelForm):
    class Meta:
        model=User
        
        # Copy Modes fields and show 
        fields=('name','email','password')
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(render_value=True,attrs={'class':'form-control'})
        }