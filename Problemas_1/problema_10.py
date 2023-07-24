"""10- Los N empleados de una empresa reciben un salario por semana de acuerdo con las
horas trabajadas. Las horas normales de trabajo por semana son 40 y las horas
adicionales se pagan al doble de las horas normales. Escribir un algoritmo que solicite
las horas trabajadas en la semana por cada empleado y la paga por hora trabajada,
para calcular a) el monto que debe recibir el empleado, b) el monto total requerido para
el pago a todos los empleados, y c) la cantidad de billetes de cada denominaciån que
se requiere para efectuar el pago a los empleados."""

cantidad_empleados = int(input("Cantidad de empleados: "))

suma_pagas = 0
for i in range(cantidad_empleados):
    horas_trabajadas = int(input(f"Horas trabajadas de empleado {i + 1}: "))
    paga_por_hora = int(input(f"Pago por hora del empleado {i + 1}: "))

    if (horas_trabajadas > 40):
        paga = (40*paga_por_hora) + ((horas_trabajadas - 40) * (2*paga_por_hora))
    else:
        paga = paga_por_hora * horas_trabajadas
    suma_pagas += paga
    print(f"La paga del empleado {i + 1} es: {paga}")
print(f"El monto total requerido para pagar a todos los empleados es de: {suma_pagas}")

# 100, 50, 20, 10, 5, 1


print("Va a necesitar")
if(suma_pagas//100):
    print(suma_pagas//100, "Billetes de 100")
    suma_pagas %= 100
if(suma_pagas//50):
    print(suma_pagas//50, "Billetes de 50")
    suma_pagas %= 50
if(suma_pagas//20):
    print(suma_pagas//20, "Billetes de 20")
    suma_pagas %= 20
if(suma_pagas//10):
    print(suma_pagas//10, "Billetes de 10")
    suma_pagas %= 10
if(suma_pagas//5):
    print(suma_pagas//5, "Billetes de 5")
    suma_pagas %= 5
if(suma_pagas//1):
    print(suma_pagas//1, "Billetes de 1")
    suma_pagas %= 1

