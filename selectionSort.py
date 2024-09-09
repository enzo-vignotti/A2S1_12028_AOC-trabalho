V = [5,4,3,2,1,0]

comeco = 0
tamLista = len(V)

while (comeco - tamLista < 0):
    menor = V[comeco]
    inicio = comeco
    while (inicio - tamLista < 0):
        if (V[inicio] - menor < 0):
            menor = V[inicio]
            V[inicio] = V[comeco]
            V[comeco] = menor
        inicio += 1
    comeco += 1

print(V)