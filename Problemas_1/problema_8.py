"""8- Para elaborar la planilla de evaluaciån de un curso de N alumnos, se requiere un
algoritmo que reciba como datos para cada alumno: a) nota obtenida en el examen
parcial; y b) nota obtenida en el examen final. A partir de estos elementos, se debe
calcular la nota final para cada alumno y el promedio general del curso.
El procedimiento de cålculo es el siguiente:
Calificaciån = 0.4 (nota examen parcial) + 0.6 (nota examen final)
Calificaciån      Nota final
0-59              1
60 - 69           2
70 - 79           3
80-89             4
90 - 100          5
"""

cantidad_alumnos = int(input("Ingrese la cantidad de alumnos: "))
suma = 0

for i in range(1, cantidad_alumnos + 1):
    parcial = int(input("Nota en el examen parcial: "))
    final = int(input("Nota en el examen final: "))

    calificacion = 0.4*parcial + 0.6*final
    nota = 0
    if(calificacion < 60):
        nota = 1
    elif(calificacion < 70):
        nota = 2
    elif(calificacion < 80):
        nota = 3
    elif(calificacion < 90):
        nota = 4
    else:
        nota = 5
    print(f"La nota final del alumno {i} es: {nota}")
    suma += nota
print("El promedio general de la clase es: ", suma/cantidad_alumnos)