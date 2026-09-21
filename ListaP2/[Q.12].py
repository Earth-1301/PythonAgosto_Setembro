C=200
O=-1
TEnt=0
TSai=0
Ent=0
Sai=0
SaiEr=0
while O!=0:
    O=int(input("Escreva a Operação\n1 para 'Entrada'\n2 para 'Saída'\n0 para 'Fim'\n=>"))
    if O==1:
        N=int(input("Valor da Entrada\n=>"))
        C+=N
        Ent+=1
        TEnt+=N
    elif O==2:
        N=int(input("Valor da Saída\n=>"))
        if N>C:
            print("Valor Insuficiente")
            SaiEr+=1
        else:
            C-=N
            Sai+=1
            TSai+=N
    elif O==0: 
        print("Processo Terminado")
    else:
        print("Tente de Novo")
print("Saldo Final\n=>",C,"\nEntradas\n=>",Ent,"\nSaídas\n=>",Sai,"\nRetiradas Recusadas\n=>",SaiEr,"\nTotal Adicionado\n=>",TEnt,"\nTotal Removido\n=>",TSai)