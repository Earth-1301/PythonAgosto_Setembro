L=[]
X=0
Y=0
for i in range(6):
    N=int(input("Escreva uns Números\n=>"))
    L.append(N)
T2=tuple(L)
for i in T2:
    if i==5:
        X=X+1
if X >=1:
    H=T2.index(5)
else:
    H='Não tem 5'
for i in T2:
    if i%2==0:
        Y=Y+1
print("Quantas Vezes o Número 5 apareceu\n=>",X,"\nPosição do Número 5\n=>",H,"\nNúmero de Números Pares\n=>",Y)