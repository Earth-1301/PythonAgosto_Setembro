VenTot=[]
MaiVen=[]
AciMed=[]
MaiVal=0
for i in range(5):
    Ven={'Nome':str(input("Cadastre O Nome\n=>")),'Vendas':[]}
    for n in range(4):
        Ven['Vendas'].append(float(input("Insira O Valo Das Vendas\n=>")))
    VenTot.append(Ven)
ValTot=0
for i in VenTot:
    SomVen=0
    for n in i['Vendas']:
        SomVen+=n
    i['Total']=SomVen
    ValTot+=SomVen
    if MaiVal<i['Total']:
        MaiVal=i['Total']
Med=ValTot/len(VenTot)
for i in VenTot:
    print("Nome\n=>",i['Nome'],"\nTotal Vendido\n=>",i['Total'])
    if i['Total']==MaiVal:
        MaiVen.append(i['Nome'])
    if i['Total']>Med:
        AciMed.append(i['Nome'])
print("Total Vendido\n=>",ValTot,"\nVendedor(es) Com A Maior Venda\n",MaiVen,"\nVendedores Acima Da Média\n=>",AciMed)