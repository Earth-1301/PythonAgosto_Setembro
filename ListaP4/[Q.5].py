L=[{'Código':'101A','Nome':'Arroz','Preço':24.99,'Quantidade':12},{'Código':'102B','Nome':'Açucar','Preço':3.99,'Quantidade':24},{'Código':'103C','Nome':'Leite','Preço':4.99,'Quantidade':36},{'Código':'104D','Nome':'Café','Preço':25.50,'Quantidade':48},{'Código':'105E','Nome':'Pão','Preço':7.99,'Quantidade':60}]
for i in range(5):
    O=str(input("Digite 'E' Para Entrada\nDigite 'S' Para Saída\n=>"))
    if O == 'E':
        Cod=str(input("Escreva O Código Do Produto\n=>"))
        for i in L:
            Loc=-1
            if i['Código']==Cod:
                Loc=-1
                Loc=L.index(i)
                print("Quantidade Disponível\n=>",L[Loc]['Quantidade'])
                L[Loc]['Quantidade']+=int(input("Entrada\n=>"))
        if Loc<0:
            print("Código Não Encontrado")
    elif O == 'S':
        Cod=str(input("Escreva O Código Do Produto\n=>"))

        for i in L:
            Loc=-1    
            if i['Código']==Cod:
                Loc=L.index(i)
                print("Quantidade Disponível\n=>",L[Loc]['Quantidade'])
                S=int(input("Saída\n=>"))
                if S<L[Loc]['Quantidade']:
                    L[Loc]['Quantidade']-=S
                else:
                    print("Quantidade Inválida")
        if Loc<0:
            print("Código Não Encontrado")
    else:
        print("Opção Inválida")
for i in L:
    print("Nome\n=>",i['Nome'],"\nQuantidade\n=>",i['Quantidade'],"\nValor Financeiro\n=>",round(i['Quantidade']*i['Preço'],2))