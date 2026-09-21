L={'Mentos':1.75,'Paçoquinha':0.75,'Chiclete':0.25,'Gomas':1.50,'Piruluito':1 }
N=str(input("Escreva o Nome do Produto\n=>"))
if N in L:
    print("Preço\n=>",L[N])
else:
    print("O Produto Não Está Cadastrado")