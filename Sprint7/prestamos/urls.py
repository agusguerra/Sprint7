from django.urls import path
from . import views

#URLconf de prestamos
urlpatterns = [
    path('', views.prestamos_view, name='prestamo'),
    path('nuevo-prestamo', views.sacar_prestamo, name='nuevo-prestamo')
]