lista_R = [1,2,3,4,5,6,7,8,9,10]
lista_S = [11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

vector_X = lista_R + lista_S

vector_W = []

for i in range(10):
    vector_W.append(lista_R[i])
    vector_W.append(lista_S[i])

print(vector_W)

vector_Z = []

for i in lista_R:
    if i not in lista_S:
        vector_Z.append(i)
for i in lista_S:
    if i not in vector_Z:
        vector_Z.append(i)

print(vector_Z)