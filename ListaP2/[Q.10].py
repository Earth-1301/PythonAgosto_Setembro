Pri=[]
D=0
A=int(input("Escreva um Número Positivo\n=>"))
while A<0:
    A=int(input("Tente de Novo\n=>"))
B=int(input("Escreva um Número Positivo Maior que 'A'\n=>"))
while B<A:
    B=int(input("Tente de Novo\n=>"))
X=A
Y=1
Div=0
while X<=B:
    while Y<=X:
        if X%Y == 0:
            D+=1
        Y+= 1
    if D==2:
        Pri.append(X)
    D=0
    X+=1
    Y=1
print(Pri)