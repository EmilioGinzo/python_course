# 2- Generar todos los términos de la serie: 8, 13, 18, 23 necesarios para que la suma de los términos sea igual a 426.
numero = 8
suma = 0
while ( suma < 426):
    suma += numero
    print(numero, end=", ")
    numero += 5
print()
print(suma)