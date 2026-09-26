Con={}
Nom='A'
while Nom !='FIM':
    Nom=str(input("Escreva O Nome Do Contado\n'FIM' Para Encerrar Processo\n=>"))
    if Nom not in Con and Nom !='FIM':
        Num=int(input("Escreva O Número\n=>"))
        T=0
        for i in Con:
            if Con[i]==Num:
                T=1
        if T==0:
            print("Contado Adicionado")
            Con[Nom]=Num
        else:
            print("Número Já Adicionado")
    elif Nom in Con:
        print("Nome Já Selecionado")
    else:
        print("Processo Finalizado")
Tel=str(input("Escreva O Nome Que Deseja Consultar\n=>"))
if Tel in Con:
    print("Número Do Contato\n=>",Con[Tel])
else:
    print("Contato Não Encontrado")
