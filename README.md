# Sprint7
Superuser: agustin
Password: 1234

Another users: (customer_name+customer_surname+customer_id)
e.g: lesliemoses2
Password: 1234

# UPDATE Y CORRECCIONES
 Finalización de Sprint7 aplicando todas las correcciones que hacían falta de la entrega anterior, e incluyendo nuevas características.
 
 # Previsualización del Inicio
 
![image](https://user-images.githubusercontent.com/105322348/188300505-d76ec7c0-5f5c-4bda-809b-ef9cd72f0d77.png)
![image](https://user-images.githubusercontent.com/105322348/188300516-a61aa44a-713c-42c9-939c-61bbd8da2ba5.png)

# Inicio de Sesión

![image](https://user-images.githubusercontent.com/105322348/188300595-2928150b-7885-4187-ae1a-9dc710a416a0.png)

# Dashboard

 Los datos del dashboard correspondiente a cada usuario son tomados de la base de datos mediante **querys** realizadas dentro de las **view-function** de la respectiva app, y pasando diccionarios **context** a los **templates**. También se utilizaron **template tags** dentro de los archivos html para la lógica de cargado de las distintas "perspectivas" de los usuarios. Por ejemplo según el tipo de tarjeta de la cuenta del usuario, aparecerá una imágen de Visa, de Mastercard, de AmEx o de Maestro. Por otra parte, si el usuario no posee cuenta se visualizará un mensaje "el usuario no posee cuenta" y no visualizará ninguna tarjeta, como tampoco le aparecerá la opción para realizar un préstamo.
 
 ![image](https://user-images.githubusercontent.com/105322348/188300781-e4d44882-ebbe-43f2-921d-7ea62d4148af.png)

# Notificación de Préstamo
 Según el tipo de cliente, el usuario podrá visualizar una tarjeta "tienes un préstamo disponible" acompañado con el monto máximo preaprobado que le corresponda.
 
 ![image](https://user-images.githubusercontent.com/105322348/188300983-55378d85-5f2c-4345-98ea-abc52aab969d.png)

# Página para Pedir un Préstamo
 Al hacer clic en la tarjeta del préstamo preaprobado se redirige a una página de diseño sobrio, que permite realizar dicho préstamo. 
 
 ![image](https://user-images.githubusercontent.com/105322348/188301160-f4eeb6c6-adad-40a3-bae8-87a823b4efab.png)
 
 Tiene una sección de "más información" que le informará el funcionamiento de los mismos, como ser que nuestros présamos tienen un interés del **50% anual**. Por ejemplo, si se paga en 6 meses el interés será del 25%. Si se paga en 24 meses el interés asciende al 100%, y así sucesivamente. 
 
 ![image](https://user-images.githubusercontent.com/105322348/188302288-162bc64b-04fb-406b-a433-e72c275bf6a4.png)
 
 El **form** para sacar el préstamo se envía utilizando el método **POST**. Se contempla y valida el límite monetario que tiene cada cliente para pedir su préstamo.
 La información será obtenida en una **view** utilizando **request.POST.get()**
 Cuando se confirma el préstamo, se cargará en la **database** creando un objeto de préstamo: **Prestamo.objects.create(...)**

# Página de Aceptación del Préstamo
 Una vez realizado el préstamo, el usuario será redirigido a un **template** que muestra información del préstamo recién contratado (cantidad de cuotas y monto de cada una, total a pagar, fecha de la última cuota según los meses ingresados por el usuario, e interés). Además la página cuenta con un historial de los préstamos realizados por el mismo usuario, que se toman de la base de datos del sprint6.  
 
 ![image](https://user-images.githubusercontent.com/105322348/188301940-33ce5242-9c30-46b8-b4c6-50e6951f296a.png)

# ¿Cómo organizamos el Sprint?
 El proyecto **Django** está organizado en 6 (seis) **apps: Clientes, Cuentas, Homepage, Login, Prestamos, Tarjetas**, y el directorio main llamado **sprint7**.
 
 ![image](https://user-images.githubusercontent.com/105322348/188302163-ee5ca2fb-37d7-4b20-be05-2000a4dd55e9.png)

 Se decidió mantener a todos los modelos **models.py** en la app **cuentas**. Esta app también tiene un archivo de migración *0002_auto_20220831_0444* donde se corre un script que genera un usuario por cada cliente existente en la base de datos.
 
 Los directorios de **static** y de **templates** están organizados según su app. La app *cuentas* tiene el template del *dashboard*; la app *login* tiene el template para iniciar sesión; la app *homepage* tiene los templates relacionados al inicio, como el *home*, *dolar* y el *navbar*. Por su parte, la app de *prestamos* tiene los templates para sacar el *prestamo* y del *prestamo_sacado*.
 
 
 # 404
  Por último agregamos una página de **error 404** para algunos redirect de páginas no existentes.
  
  ![image](https://user-images.githubusercontent.com/105322348/188302752-187fd820-a07a-4c01-9c15-49bc40624a58.png)


