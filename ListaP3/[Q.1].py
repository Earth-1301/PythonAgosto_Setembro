L=[]
P=[]
I=[]
for i in range(10):
    N=int(input("Escreva uns Números\n=>"))
    L.append(N)
for i in L:
    if i%2==0:
        P.append(i)
    else:
        I.append(i)
print("Lista completa: ",L,"\nPares: ", P, "\nImpares: ",I)
