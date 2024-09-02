from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Flan, Pasteles
from .forms import ContactDataModelForm
from .models import ContactForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def about(request):
    
    return render(request, 'about.html')

def contacto(request):
    
    if request.method == 'POST':
        form = ContactDataModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exito')
        
    else:
        form = ContactDataModelForm()
    
    return render(request, 'contacto.html', {'form': form})

def exito(request):
    return render(request, 'exito.html')

def index(request):
    
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request, 'index.html', {'flanes': flanes_publicos})

@login_required
def bienvenido(request):
    
    flanes_privados = Flan.objects.filter(is_private=True)
    return render(request, 'bienvenido.html', {'flanes': flanes_privados})

def pasteles(request):
    
    Pasteles_privados = Pasteles.objects.filter(is_private=True)
    return render(request, 'pasteles.html', {'pasteles': Pasteles_privados})

'''

def bienvenido(request):
    return render(request, 'bienvenido.html')
    '''