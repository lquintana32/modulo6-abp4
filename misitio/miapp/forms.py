from django import forms

class UsuarioForm(forms.Form):
    nombre = forms.CharField(max_length=50,required=True)
    apellido = forms.CharField(max_length=50,required=True)
    email = forms.EmailField(required=True)
    area = forms.CharField(max_length=50,required=True)