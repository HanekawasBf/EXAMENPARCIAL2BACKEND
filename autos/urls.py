from django.urls import path

from . import views

app_name = "autos"

urlpatterns = [
    path("", views.lista_autos, name="lista"),
    path("nuevo/", views.agregar_auto, name="agregar"),
]
