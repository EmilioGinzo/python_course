#5- Encontrar el numero entero N tal que la suma de todos los enteros de 1 hasta N es igual a 10 veces el valor de N.

# sumatoria de 1 hasta n = 10n
# formula de suma de n terminos = n/2*(a1+an)

N = 1
suma = 0
while ( suma != 10 * (N)):
    N += 1
    suma = N/2*(1+N)
print(N)
