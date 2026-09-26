Est={'101A':12,'102B':24,'103C':36,'104D':48,'105D':60}
Ent=[]
Sai=[]
Err=[]
for i in range(6):
    T=(str(input("Escreva O Código Do Produto\n=>")),str(input("Escreva\n'E' Para Entrada\n'S' Para Saída\n=>")),int(input("Escreva A Quantidade\n=>")))
    if T[0] in Est:
        if T[1]=='E':
            Est[T[0]]+=T[2]
            Ent.append(T)
        elif T[1]=='S':
            if T[2]<=Est[T[0]]:
                Est[T[0]]-=T[2]
                Sai.append(T)
            else:
                Err.append(T)
        else:
            Err.append(T)
    else:
        Err.append(T)
print("Estoque Atual\n=>",Est,"\nHistórico De Entradas",Ent,"\nHistórico De Saída",Sai,"\nOperações Recusadas",Err)