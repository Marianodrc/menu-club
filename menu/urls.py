from django.urls import path
from . import views

urlpatterns = [
    # Esta es la ruta principal que verá el cliente
    path('', views.ver_menu, name='ver_menu'), 
]