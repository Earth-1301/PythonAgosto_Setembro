JogTot=[]
P=[]
Mai=0
MenPon=[]
MaiPon=[]
TotPon=0
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
    TotPon+=i['Total']
Men=JogTot[0]['Total']
MedTot=TotPon/(len(JogTot)*len(JogTot[0]['Ponto']))
MenDif=MedTot-JogTot[0]['Média']
if MenDif<0:
    MenDif*=-1
for i in JogTot:
    if i['Total']<Men:
        Men=i['Total']
    if i['Total']>Mai:
        Mai=i['Total']
    Dif=MedTot-i['Média']
    if Dif<0:
        Dif*=-1
    if Dif<MenDif:
        MaiMed=i['Média']
        MenDif=Dif
for i in JogTot:
    if i['Total']==Men:
        MenPon.append(i['Nome'])
    elif i['Total']==Mai:
        MaiPon.append(i['Nome'])
    if i['Média']==MaiMed:
        MedNom=i['Nome']
for i in JogTot:
    print("Nome Do Jogado\n=>",i['Nome'],"\nTotal De Pontos\n=>",i['Total'],"\nMédia\n=>",i['Média'])
print("Média de Pontos\n=>",MedTot,"\nJogadores Com A Maior Pontuação\n=>",MaiPon,"\nJogadores Com A Menor Pontuação\n=>",MenPon,"\nJogador Mais Mediano\n=>",MedNom)