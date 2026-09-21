M = int(input("Escreva um Número: "))
M2 = int(input("Digite Outro Número: "))
if M < M2:
    X = M2
    M2 = M
    M = X
for i in range(6):
    N = int(input("Escreva Mais um Número: "))
    if M2< N < M:
        M2 = N
    elif N > M:
        X = M
        M = N
        M2 = X
print("O Maior Número é ",M, "e o Segundo Maior é " ,M2 )