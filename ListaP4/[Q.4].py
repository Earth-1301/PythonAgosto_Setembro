SomTot=0
MaiMed=0
Tur=[]
AciMed=[]
Emp=[]
for i in range(6):
    Alu={'Nome':str(input("Escreva O Nome Do Aluno\n=>")),'Nota': [],}
    for i in range(3):
        Alu['Nota'].append(float(input("Escreva A Nota\n=>")))
    Som=0
    for i in Alu['Nota']:
        Som+=i
    Alu['Média']=Som/len(Alu['Nota'])
    if Alu['Média']>MaiMed:
        MaiMed=Alu['Média']
    Tur.append(Alu)
for i in Tur:
    SomTot+=i['Média']
    print("Nome Do Aluno\n=>",i['Nome'],"\nMédia\n=>",i['Média'])
    if i['Média']==MaiMed:
        Emp.append(i['Nome'])
MedTot=SomTot/len(Tur)
for i in  Tur:
    if i['Média']>MedTot:
        AciMed.append(i['Nome'])
print("Mèdia Geral Da Turma\n=>",MedTot,"\nAlunos Acima Da Média\n=>",len(AciMed),"\nAlunos Com A(s) Maior Média\n=>",Emp)