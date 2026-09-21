D=0
X = 1
N=int(input("Escreva um Número\n=>"))
while X<=N:
    if N%X == 0:
        D+=1
    X += 1
if D==2:
    print(N," é um Número Primo")
else:
    print(N," não é um Número Primo")