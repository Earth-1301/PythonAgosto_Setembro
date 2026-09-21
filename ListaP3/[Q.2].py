L=[]
for i in range(10):
    N=int(input("Escreva uns números\n=>"))
    L.append(N)
M1=L[0]
for i in L:
    if i >= M1:
        M1=i
M2=L[0]
for i in L:
    if i <= M2:
        M2=i
print("Maior Número\n=>",M1,"\nMenor Número\n=>",M2)