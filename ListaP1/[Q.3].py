L=[]
for i in range(3):
    L.append(int(input("Escreva um Número\n=>")))
M=L[0]
for i in L:
    if i > M:
        M=i
print("Maior Número\n=>",M)