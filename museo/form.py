from django import forms 

class UserForm(forms.Form):
    nombre = forms.CharField(label="nombre",max_length=150)
    password = forms.CharField(label="password",max_length=150)
    email = forms.EmailField(label='email')