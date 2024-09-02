import sys
inteiro = 10

saida = []
i = sys.getsizeof(inteiro)
while (i >= 0) :
    if (inteiro >> i) & 1:
        saida.append(1)
    else:
        saida.append(0)
    i -= 1
print(saida)

print('\n INVERTIDO')

saida = []
invertido = ~inteiro
i = sys.getsizeof(invertido)
while (i >= 0) :
    if (invertido >> i) & 1:
        saida.append(1)
    else:
        saida.append(0)
    i -= 1
print(saida)

print('TESTES DE MULTIPLICAÇÃO E DIVISÃO')

a = 20
b = a << 50
c = a * (2**50)
print(a)
print(b)
print(c)