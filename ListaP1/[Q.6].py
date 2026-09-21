L=[]
P=[]
for i in range(10):
    L.append(int(input("Escreva um Número\n=>")))
for i in L:
    if i%2==0:
        P.append(i)
print("Totais de Números Pares\n=>",len(P))