"""12- Calcular el mayor elemento en una serie de nümeros positivos. El ültimo elemento tiene
un valor -1 y no debe ser procesado."""

maximo = 0

numero = 1
while( numero != -1 ):
    numero = int(input(f"Numero : "))
    if( numero == -1):
        break
    if ( numero > maximo ):
        maximo = numero

print("El menor numero es:", maximo)