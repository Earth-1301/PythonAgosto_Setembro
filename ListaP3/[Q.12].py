L=[]
ValTot=0
IteCad=0
M=0
for i in range(5):
    L.append({'Cod':str(input("Código Do Produto\n=>")),'Nom':str(input("Nome Do Produto\n=>")),'Qua':int(input("Quantidade Do Produto\n=>")),'Pre':float(input("Preço Do Produto\n=>"))}) 
for i in L:
    print("Itens Disponíveis\n=>",i['Nom'])
    ValTot+=i['Pre']*i['Qua']
    if i['Pre']*i['Qua']>M:
        M=i['Pre']*i['Qua']
        MaiNom=i['Nom']
    IteCad+=i['Qua']
T=(IteCad,ValTot)
print("Valor Total Do Estoque\n=>",ValTot,"\nItem de Maior Valor\n=>",MaiNom,"\nQuantidade De Itens Cadastrados\n=>",T[0],"\nValor Total No Estoque\n=>",T[1])