import re
from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from .forms import UsuarioForm

# Create your views here.
def index(request):
    return render(request,'miapp/index.html')

def formulario(request):
    return render(request,'miapp/formulario.html')

def create(request):
    form=UsuarioForm()
    if request.method == 'POST':
        form=UsuarioForm(request.POST)
    if form.is_valid():
        usuario = Usuario()
        usuario.nombre = form.cleaned_data['nombre']
        usuario.apellido = form.cleaned_data['apellido']
        usuario.email = form.cleaned_data['email']
        usuario.area = form.cleaned_data['area']
        usuario.save()
    else:
        pass
    return render(request, 'miapp/create.html', {'form':form})
    
 