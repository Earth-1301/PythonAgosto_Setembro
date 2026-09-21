M=0
T=(0,0)
L=[]
Q1=[]
Q2=[]
Q3=[]
Q4=[]
for i in range(6):
    L.append((int(input("Escreva Uma Coordenada X\n=>")),int(input("Escreva Uma Coordenada Y\n=>"))))
for i in L:
    if i[0]>0 and i[1]>0:
        Q1.append(i)
    elif i[0]>0 and i[1]<0:
        Q2.append(i)
    elif i[0]<0 and i[1]<0:
        Q3.append(i)
    elif i[0]<0 and i[1]>0:
        Q4.append(i)
    if i[0]**2+i[1]**2>T[0]**2+T[1]**2:
        del T
        T=i
print("Primeiro Quadrante\n",Q1,"\nSegundo Quadrante\n=>",Q2,"\nTerceiro Quadrante\n=>",Q3,"\nQuarto Quadrante\n=>",Q4,"\nMaior Valor De X^2+Y^2\n=>",T)