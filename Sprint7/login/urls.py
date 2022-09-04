from django.urls import path
from . import views

#URLconf de login
urlpatterns = [
    path('', views.loginPage, name="login"),
    path('logout/', views.logoutPage, name="logout"),
    
]