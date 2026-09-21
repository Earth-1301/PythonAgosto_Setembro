Dic={}
Emp={}
MFre=0
for i in range(10):
    Nom=str(input("Escreva Um Nome\n=>"))
    if Nom in Dic:
        Dic[Nom]+=1
    else:
        Dic[Nom]=1
for i in Dic:
    if Dic[i]>MFre:
        MFre=Dic[i]
for i in Dic:
    if Dic[i]==MFre:
        Emp[i]=Dic[i]
print("Palavras E Suas Quantidades\n=>",Dic,"\nPalavras Com O Maior Número De Repetição\n=>",Emp)