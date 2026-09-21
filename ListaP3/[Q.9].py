Dic={'Arroz':12,'Leite':12,'Café':12,'Açucar':12}
Pro=str(input("Escreva O Nome De Um Produto\n=>"))
if Pro in Dic:
    Q=int(input("Escreva A Quantidade Vendida\n=>"))
    if Q<Dic[Pro]:
        Dic[Pro]-=Q
    else:
        print("Estoque Insuficiente")
print(Dic)