from django.urls import path
from . import views

urlpatterns = [
    path("cadastrar/", views.cadastrar, name="cadastrar_professores"),
    path("lista/", views.lista, name="lista_professores"),
]