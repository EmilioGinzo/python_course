"""11- Calcular el menor elemento en una serie de N nümeros."""

cantidad_numero = int(input("Cantidad de numeros: "))
minimo = 999999999999999999

for i in range(cantidad_numero):
    numero = int(input(f"Numero {i + 1}: "))

    if ( numero < minimo):
        minimo = numero

print("El menor numero es:", minimo)