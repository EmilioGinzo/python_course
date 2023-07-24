"""7-
Para obtener el total de ventas realizadas, una empresa comercial desea ingresar las
facturas procesadas en el dia. Las facturas pueden ser al contado, tipo (1), o a crédito,
tipo (2), y se desean totales separados para cada tipo. No se conoce el total de
facturas, y por ello, el proceso deberå concluir cuando se ingrese una factura de tipo
(O). Escribir un algoritmo para realizar esta funciån."""


tipo_factura = int(input("Ingrese el tipo de factura: "))
monto = int(input("Ingrese el monto: "))

suma_factura_tipo_contado = 0
suma_factura_tipo_credito = 0
while(tipo_factura != 0):
    if (tipo_factura == 1):
        suma_factura_tipo_contado += monto
    elif(tipo_factura == 2):
        suma_factura_tipo_credito += monto
    else:
        print("Ingrese un tipo de factura valido")
    tipo_factura = int(input("Ingrese el tipo de factura: "))
    if (tipo_factura > 2 or tipo_factura == 0):
        continue
    monto = int(input("Ingrese el monto: "))
print("Total al contado:", suma_factura_tipo_contado)
print("Total a credito:", suma_factura_tipo_credito)
