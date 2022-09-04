from multiprocessing import context
from django.shortcuts import render
from cuentas.models import Cuenta, Prestamo, Tiposclientes, Cliente
from django.contrib.auth.decorators import login_required
from datetime import date, timedelta

# Create your views here.

# Vista principal para sacar los préstamos
@login_required(login_url='login')
def prestamos_view(request):
 
    # Lógica del límite de prestamo según el tipo de cliente:
    cliente = Cliente.objects.get(customer_id = request.user.id)
    tipo_cliente = Tiposclientes.objects.get(tipoid = cliente.tipoid.tipoid)


    if (tipo_cliente.tipoid == 1): # Classic
        limite_prestamo = 100000
    elif (tipo_cliente.tipoid == 2): # Gold
        limite_prestamo = 300000
    elif (tipo_cliente.tipoid == 3): # Black
        limite_prestamo = 500000

    context = {
        'limite_prestamo': limite_prestamo,
    }
    

    return render(request, 'prestamos.html', context)


# Vista para cuando ya sacaste un préstamo
@login_required(login_url='login')
def sacar_prestamo(request):
    customer_id_ = request.user.cliente.customer_id
    loan_type_ = request.POST.get("prestamo-tipo")

    # "aux_date" es la cantidad de meses que el cliente elige para pagar
    aux_date = request.POST.get('prestamo-fecha')
    
    # "loan_date" es la fecha actual en la que saca el préstamo
    loan_date_ = date.today()

    fecha_pago_prestamo = loan_date_ + timedelta(int(aux_date)*30)

    loan_total_ = request.POST.get('prestamo-monto')
    
    Prestamo.objects.create(
        customer_id = customer_id_,
        loan_type = loan_type_,
        loan_date = loan_date_,
        loan_total = loan_total_
    )

    cuenta = Cuenta.objects.filter(customer_id = customer_id_).first()
    balance_ = cuenta.balance
    cuenta_id_ = cuenta.account_id

    Cuenta.objects.filter(account_id = cuenta_id_).update(balance = balance_+int(loan_total_))

    # La tasa de interes es del 50% anual para nuestro Homebanking!! :D
    interes = ( int(aux_date) / 12) * 0.5
    print(interes)
    lo_que_debo_pagar = (float(loan_total_) * interes) + float(loan_total_)
    cuota = lo_que_debo_pagar / int(aux_date)

    listado_prestamos = Prestamo.objects.filter(customer_id=request.user.cliente.customer_id).all()
    interes_porcentaje = interes*100


    context = {
        'customer_id': customer_id_,
        'loan_type': loan_type_,
        'loan_date_': loan_date_,
        'aux_date': aux_date,
        'loan_total': loan_total_,
        'fecha_pago_prestamo': fecha_pago_prestamo,
        'interes_porcentaje': interes_porcentaje,
        'lo_que_debo_pagar': lo_que_debo_pagar,
        'cuota': cuota,
        'listado_prestamos': listado_prestamos,
    }        

    return render(request, 'prestamo_sacado.html', context)






    
