L = []
for i in range(8):
    N = int(input("Escreva um número: "))
    L.append(N)
V = max(L)
P = L.index(V)
print("A Posição do Maior Número na Lista é ", P+1, " e o Maior Número é: ", V)
#O "for" repete para o usuário digitar 8 vezes
#O "append" coloca os números em uma lista e o "index" mostra a posição do número
#No final, imprime um número maior pois a lista começa a contar do zero