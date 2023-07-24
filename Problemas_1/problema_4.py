# 4- Hallar la suma de los términos de Ia serie: 1/1! + 1/2! + 1/3! + ....+ 1/N!

cantidad = int(input('Ingrese N: '))

numero = 1
suma = 0
for i in range(1, cantidad + 1):
    numero /= i
    suma += numero
print(suma)
