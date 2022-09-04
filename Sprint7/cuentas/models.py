# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

class AuditoriaCuenta(models.Model):
    old_id = models.IntegerField()
    new_id = models.IntegerField()
    old_balance = models.IntegerField()
    new_balance = models.IntegerField()
    old_iban = models.TextField()
    new_iban = models.TextField()
    old_type = models.TextField()
    new_type = models.TextField()
    user_action = models.TextField()
    created_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'Auditoria_Cuenta'


class Marcatarjeta(models.Model):
    marcaid = models.AutoField(primary_key=True)
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'MarcaTarjeta'


class Tipocuenta(models.Model):
    tipocuentaid = models.AutoField(primary_key=True)
    name = models.TextField()

    def __str__(self):
        return f"{self.tipocuentaid}"

    class Meta:
        managed = False
        db_table = 'TipoCuenta'


class Tiposclientes(models.Model):
    tipoid = models.AutoField(primary_key=True)
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'TiposClientes'



class Sucursal(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_number = models.BinaryField()
    branch_name = models.TextField()
    branch_address_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sucursal'


class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField()
    customer_surname = models.TextField()  # This field type is a guess.
    customer_dni = models.TextField(unique=True)
    dob = models.TextField(blank=True, null=True)
    branch_id = models.ForeignKey(Sucursal, db_column='branch_id', default=None, on_delete=models.CASCADE)
    tipoid = models.ForeignKey(Tiposclientes, db_column='tipoid', default=None, on_delete=models.CASCADE)
    #Tabla user_id que es un FK a la tabla User propia de Django
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE, related_name='cliente')

    def __str__(self):
        return f"{self.customer_name} {self.customer_surname}"

    class Meta:
        managed = False
        db_table = 'cliente'


class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Cliente, db_column="customer_id", default=None, on_delete=models.CASCADE)
    balance = models.IntegerField()
    iban = models.TextField()
    tipocuentaid = models.ForeignKey(Tipocuenta, models.DO_NOTHING, db_column='tipocuentaid', default=None)

    def __str__(self):
        return "(" + str(self.account_id) + ', ' + str(self.customer_id) + ', ' + str(self.balance) + ', ' + str(self.iban) + ', ' + str(self.tipocuentaid) + ")"

    class Meta:
        managed = False
        db_table = 'cuenta'


class Empleado(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.TextField()
    employee_surname = models.TextField()
    employee_hire_date = models.TextField()
    employee_dni = models.TextField()
    branch_id = models.ForeignKey(Sucursal, db_column='branch_id', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'empleado'


class Movimientos(models.Model):
    mov_id = models.AutoField(primary_key=True)
    nro_cuenta = models.ForeignKey(Cuenta, models.DO_NOTHING, db_column='nro_cuenta')
    monto = models.IntegerField()
    op_type = models.TextField()
    hora = models.DateField()

    class Meta:
        managed = False
        db_table = 'Movimientos'


class Direcciones(models.Model):
    calle = models.TextField(primary_key=True)
    numero = models.IntegerField()
    ciudad = models.TextField()
    provincia = models.TextField()
    pais = models.TextField()
    customer = models.ForeignKey(Cliente, models.DO_NOTHING, blank=True, null=True, db_column='customer_id')
    employee = models.ForeignKey(Empleado, models.DO_NOTHING, blank=True, null=True, db_column='employee_id')
    branch = models.OneToOneField(Sucursal, models.DO_NOTHING, blank=True, null=True, db_column='branch_id')

    class Meta:
        managed = False
        db_table = 'direcciones'


class Prestamo(models.Model):
    loan_id = models.AutoField(primary_key=True)
    loan_type = models.TextField()
    loan_date = models.TextField()
    loan_total = models.IntegerField()
    customer_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'prestamo'


class Tarjeta(models.Model):
    numerotarjeta = models.AutoField(primary_key=True)
    cvv = models.IntegerField()
    fecha_de_otorgamiento = models.DateField()
    fecha_de_expiracion = models.DateField()
    tipo_tarjeta = models.TextField()
    marcaid = models.ForeignKey(Marcatarjeta, models.DO_NOTHING, db_column='marcaid')
    customer_id = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True, db_column='customer_id')

    class Meta:
        managed = False
        db_table = 'tarjeta'
