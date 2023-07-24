# serie a

cadena = ""
for i in range(1, 10):
    cadena += str(i)
    print(cadena)


#serie b

for i in range(1, 9):
    for j in range(i):
        print(i, end="")
    print()

# serie c

for i in range(1, 14):
    for j in range(i, i + 4):
        print(j, end="")
    print()

# serie d

for i in range(1, 10):
    for j in range(1, i):
        print(j, end="")
    print(i, end="")
    for j in reversed(range(1, i)):
        print(j, end="")
    print()

# serie e

cadena = "1234"
for i in range(1, 5):
    for j in range(i, 5):
        print(j, end="")
    for j in range(1, i):
        print(j,end="")
    print()
