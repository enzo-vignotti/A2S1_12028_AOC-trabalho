bn = 2
qtd = 4
razao = 2
while (1 - qtd < 0):
    bn *= razao
    qtd -= 1

print(bn)