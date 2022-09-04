from django.urls import path
from . import views

#URLconf
urlpatterns = [
    path('', views.dash),
    path('404', views.error404),
]

