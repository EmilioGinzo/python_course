"""15- Considerando el conjunto de nümeros naturales entre 1 y 99, escribir algoritmos
apropiados para calcular e imprimir :"""

# Aquellos que son cuadrados de otros valores del mismo grupo.
import math


for i in range(math.ceil(math.sqrt(99))):
    print("Estos numeros son cuadrados de otros:", i*i)

#Los grupos de tres nümeros que pueden representar los lados de un triångulo
#rectångulo (ej: 3, 4 y 5) y cuåles son dichos grupos. (la suma de dos lados tiene que ser mayor al tercero)

for i in range(1, 100):
    for j in range(i, 100):
        for k in range(j, 100):
            if (i != j and j != k and i != k and i + j > k):
                print("Estos tres numeros hacen un triangulo:", i, j, k)


#En cuåntos de ellos la primera cifra es mayor que la segunda cifra y cuåles son dichos nümeros.

print("Estos numeros tienen la primera cifra mayor a la segunda: ")
for i in range(10, 100):
    primera_cifra = i//10
    if (primera_cifra > i%10):
        print(i)

#Todos los que sean nümeros primos.

for i in range(1, 100):
    primo = True
    for j in range(2, (math.ceil(math.sqrt(i)) + 1 )):
        if ( i % j == 0 and i != j):
            primo = False
    if primo:
        print(i)