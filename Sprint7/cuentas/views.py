from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Cuenta, Marcatarjeta, Tiposclientes
from .models import Tipocuenta
from .models import Tarjeta
from .models import Cliente
from django.contrib.auth.models import User
# Create your views here.

@login_required(login_url='login')
def dash(request):
    #Querys para tomar datos de la base de datos y mostrar según el usuario


    # Busca match entre Cuenta & User (customer_id)

    cuenta = Cuenta.objects.filter(customer_id = request.user.id).first()
    
    if cuenta:
        # Busca match entre Tipocuenta & Cuenta (tipocuentaid)
        tipo_cuenta = Tipocuenta.objects.get(tipocuentaid = cuenta.tipocuentaid.tipocuentaid)

        # Busca match entre Tarjeta & User  (customer_id)
        tarjeta = Tarjeta.objects.get(customer_id = request.user.id)

        # Busca match entre Marcatarjeta & Tarjeta (marcaid)
        marca_tarjeta = Marcatarjeta.objects.get(marcaid = tarjeta.marcaid.marcaid)

        #Busca match entre Tiposclientes & Cliente (tipoid)
        cliente = Cliente.objects.get(customer_id = request.user.id)
        tipo_cliente = Tiposclientes.objects.get(tipoid = cliente.tipoid.tipoid)
        
    else:
        cuenta=-1
        tipo_cuenta=-1
        tarjeta=-1
        marca_tarjeta=-1
        tipo_cliente=-1

    context = {
        'cuenta': cuenta,
        'tipo_cuenta': tipo_cuenta,
        'tarjeta': tarjeta,
        'marca_tarjeta': marca_tarjeta,
        'tipo_cliente': tipo_cliente,
    }

    return render(request, 'dashboard.html', context)


def error404(request):
    return render(request, 'error404.html')



