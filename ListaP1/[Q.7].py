L=[]
P=[]
N=0
for i in range(8):
    L.append(int(input("Escreva um Número\n=>")))
for i in L:
    if i >=0:
        P.append(i)
for i in P:
    N+=i
print("Soma Total dos Números Positivos\n=>",N)
