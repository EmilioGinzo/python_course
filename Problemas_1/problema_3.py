# 3- Hallar la suma de los primeros 10 términos de la serie: 1/2,1/4,1/8,1/16


numero = 1
for i in range(1, 11):
    numero /= 2
    print(numero, end=", ")
