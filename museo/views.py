from django.shortcuts import render,redirect
from .form import UserForm
from . models import Usuario
# Create your views here.
from django.http import HttpResponse


def index(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            usuario = Usuario(
                nombre = form.cleaned_data['nombre'],
                password = form.cleaned_data['password'],
                email = form.cleaned_data['email']
            )
            usuario.save()
            return redirect("success")
    

    else:
        form = UserForm()
    return render(request,'templa.html',{'form':form})            

    
def success_view(request):
    return render(request, 'success.html')


    