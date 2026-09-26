Pro=[{'Código':'101A','Nome':'Arroz','Preço':24.99,'Quantidade':12,'Vendas':0},{'Código':'102B','Nome':'Açucar','Preço':3.99,'Quantidade':24,'Vendas':0},{'Código':'103C','Nome':'Leite','Preço':4.99,'Quantidade':36,'Vendas':0},{'Código':'104D','Nome':'Café','Preço':25.50,'Quantidade':48,'Vendas':0},{'Código':'105E','Nome':'Pão','Preço':7.99,'Quantidade':60,'Vendas':0}]
His=[]
ZerVen=[]
Cod='1'
ValTot=0
MaiVen=0
QuaVen=0
UniVen=0
while Cod!='0':
    Cod=str(input("Insira O Código\n'0' Para Finalizar\n=>"))
    if Cod!='0':
        Ven=(Cod,int(input("Insira A Quantidade\n=>")))
        His.append(Ven)
for i in His:
    Loc=-1
    for n in Pro:
        if n['Código']==i[0]:
            Loc=Pro.index(n)
    if Loc>=0:
        if Pro[Loc]['Quantidade']<=i[1]:
            Pro[Loc]['Quantidade']-=i[1]
            Pro[Loc]['Vendas']+=i[1]
            QuaVen+=1
for i in Pro:
    i['Valor']=i['Vendas']*i['Preço']
    if i['Valor']>MaiVen:
        MaiVen=i['Valor']
    if i['Vendas']==0:
        ZerVen.append(i['Nome'])
    ValTot+=i['Valor']
    UniVen+=i['Vendas']
TupRes=(QuaVen,UniVen,ValTot)
print("Histórico")
for i in His:
    print("=>",i)
for i in Pro:
    print("Estoque Restante\n=>",i['Quantidade'],"\nUnidades Vendidas\n=>",i['Vendas'],"\nValor Vendido\n=>",round(i['Valor'],2))
    if i['Valor']==MaiVen:
        MelVen=i['Nome']
print("Produto Com O Maior Valor Em Vendas\n=>",MelVen,"\nProdutos Sem Vendas\n=>",ZerVen,"\nQuantidade De Vendas,Unidades Vendidas E Valor Total\n=>",TupRes)