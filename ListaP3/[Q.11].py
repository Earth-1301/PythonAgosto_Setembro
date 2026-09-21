Pre=0
L=[('101A','Arroz','24.99'),('102B','Açucar',3.99),('103C','Leite',4.99),('104D','Café',25.50),('105E','Pão',7,99)]
Cod=str(input("Escreva O Código Do Produto\n=>"))
for i in L:
    if Cod == i[0]:
        Nom=i[1]
        Pre=i[2]
if Pre==0:
    print("Código Não Encontrado")
else:
    print("Produto\n=>",Nom,"\nPreço\n=>",Pre)