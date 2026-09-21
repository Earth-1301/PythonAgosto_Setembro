L=[]
P=[]
N=[]
S=0
X=int(input("Escreva um Número\n=>"))
if X!=0:
    L.append(X)
while X!=0:
    X=int(input("Escreva um Número ou '0' para Termintar o Processo\n=>"))
    if X!=0:
        L.append(X)
for i in L:
    if i<0:
        N.append(i)
    elif i>0:
        P.append(i)
for i in L:
    S=S+i
print("Quantidade de Números Digitados\n=>",len(L),"\nQuantidade de Números Positivos\n=>",len(P),"\nQuantidade de Números Negativos\n=>",len(N),"\nSoma Total\n=>",S)