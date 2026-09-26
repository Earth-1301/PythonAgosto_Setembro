Est=[{'Código':'101A','Nome':'Arroz','Preço':24.99,'Estoque':12},{'Código':'102B','Nome':'Açucar','Preço':3.99,'Estoque':24},{'Código':'103C','Nome':'Leite','Preço':4.99,'Estoque':36},{'Código':'104D','Nome':'Café','Preço':25.50,'Estoque':48},{'Código':'105E','Nome':'Pão','Preço':7.99,'Estoque':60}]
His=[]
Ate=[]
Rec=[]
TotVen=0
for i in range(1):
    T=(str(input("Escreva O Código\n=>")),int(input("Escreva A Quantidade\n=>")))
    His.append(T)
for i in His:
    for n in Est:
        if n['Código']==i[0]:
            Loc=Est.index(n)
        else:
            Loc=-1
        if Loc>=0:
            if i[1]<=Est[Loc]['Estoque']:
                Est[Loc]['Estoque']-=i[1]
                Ate.append(i)
                TotVen+=Est[Loc]['Preço']*i[1]
    if i not in Ate:
        Rec.append(i)
print("Histórico De Compras")
for i in His:
    print("=>",i)
print("Pedidos Atendidos")
for i in Ate:
    print("=>",i)
print("Pedidos Recusados")
for i in Rec:
    print("=>",i)
print("Valor Total Dos Pedidos Atendidos\n=>",round(TotVen,2))