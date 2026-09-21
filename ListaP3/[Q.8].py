L=[]
D={}
for i in range(8):
    L.append(str(input("Escreva Um Nome\n=>")))
for i in L:
    if i not in D:
        D[i]=1
    else:
        D[i]+=1
print(D)