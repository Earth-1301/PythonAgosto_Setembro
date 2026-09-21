JogTot=[]
P=[]
Mai=0
MenPon=[]
MaiPon=[]
for i in range(5):
    Jog={'Nome':str(input("Escreva O Nome\n=>")),'Ponto':[]}
    for i in range(3):
        Jog['Ponto'].append(int(input("Escreva A Pontuação\n=>")))
    JogTot.append(Jog)
for i in JogTot:
    Som=0
    for n in i['Ponto']:
        Som+=n
    i['Total']=Som
    i['Média']=Som/len(i['Ponto'])
Men=JogTot[0]['Total']
for i in JogTot:
    if i['Total']<Men:
        Men=i['Total']
    if i['Total']>Mai:
        Mai=i['Total']
for i in JogTot:
    if i['Total']==Men:
        MenPon.append(i['Nome'])
    elif i['Total']==Mai:
        MaiPon.append(i['Nome'])
for i in JogTot:
    print("Nome Do Jogado\n=>",i['Nome'],"\nTotal De Pontos\n=>",i['Total'],"\nMédia\n=>",i['Média'])
print("Jogadores Com A Maior Pontuação\n=>",MaiPon,"Jogadores Com A Menor Pontuação\n=>",MenPon)