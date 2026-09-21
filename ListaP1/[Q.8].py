L=[]
for i in range(6):
    L.append(int(input("Escreva um Número\n=>")))
M=L[0]
for i in L:
    if i>M:
        M=i
print("Maior Valor\n=>",M)