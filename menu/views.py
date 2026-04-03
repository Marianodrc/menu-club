from django.shortcuts import render
from .models import Categoria

def ver_menu(request):
    # Buscamos todas las categorías en la base de datos
    categorias = Categoria.objects.all()
    
    # Le enviamos esas categorías a un archivo HTML
    return render(request, 'menu/carta.html', {'categorias': categorias})