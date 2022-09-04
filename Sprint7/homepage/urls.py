from django.urls import path
from . import views

#URLconf
urlpatterns = [
    path('', views.homepage, name="home"),
    path('dolar/', views.dolar, name="dolar")
]