"""6- A fin de recaudar fondos para Ia fiesta de principio del semestre, se decide realizar una
rifa con las siguientes reglas: a) se prepara un talonario con nümeros del 1001 al 1500;
b) cada persona que adquiere la rifa debe abonar un importe igual al nümero que
elige. Suponiendo que se venden todos los nümeros, escribir un algoritmo que calcule
el monto total recaudado. El algoritmo deberå tomar como datos el nümero inicial y final
del talonario, para permitir calcular que monto se recaudaria si decidimos cambiar
estos paråmetros."""

numero_inicial = int(input("Ingrese el primer numero del talonario: "))
numero_final = int(input("Ingrese el ultimo numero del talonario: "))

suma = 0
for i in range(numero_inicial, numero_final + 1):
    suma += i

print(suma)