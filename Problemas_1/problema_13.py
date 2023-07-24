"""13- Calcular los dos valores mås pequenios en una serie de N nümeros."""

cantidad_numero = int(input("Cantidad de numeros: "))
minimo1 = 999999999999999999
minimo2 = 999999999999999999

for i in range(cantidad_numero):
    numero = int(input(f"Numero {i + 1}: "))

    if ( numero < minimo1):
        minimo1 = numero
    elif ( numero < minimo2):
        minimo2 = numero

print(f"Los dos numeros menores son: {minimo1} y {minimo2}")