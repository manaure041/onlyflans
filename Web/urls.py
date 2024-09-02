from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contacto/', views.contacto, name='contacto'),
    path('exito/', views.exito, name='exito'),
    path('bienvenido/', login_required(views.bienvenido), name='bienvenido'),
    path('pasteles/', views.pasteles, name='pasteles'),
    
    
    
]   
    