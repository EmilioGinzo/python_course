

lista = [1,1,1,1,1,1,1,1,1]

for i in range(len(lista) - 1):
    suma = 0
    for j in range(i + 1, len(lista)):
        suma += lista[j]
    lista[i] = suma