N = 0
X = int(input("Digite um número: "))
for i in range(7):
    Y = int(input("Escreva Outro Número: "))
    if X == Y:
        N=N+1
    del(X)
    X = Y
if N >= 1:
    print("Teve Números Consecutivos")
else:
    print("Não teve Números Consecutivos")
