D={'Nome':'','Turma':'','N1':'','N2':''}
D['Nome']=str(input("Escreva seu Nome\n=>"))
D['Turma']=str(input("Escreva seu Turma\n=>"))
D['N1']=int(input("Escreva sua Primeira Nota\n=>"))
D['N2']=int(input("Escreva sua Segunda Nota\n=>"))
D['M']=(D['N1']+D['N2'])/2
if D['M'] >=7:
    D['Sit']='Aprovado'
elif D['M']>=5:
    D['Sit']='Recuperação'
else:
    D['Sit']='Reprovado'
print("Nome\n=>",D['Nome'],"\nTurma\n=>",D['Turma'],"\nPrimeira Nota\n=>",D['N1'],"\nSegunda Nota\n=>",D['N2'],"\nMédia Total\n=>",D['M'],"\nSituação\n=>",D['Sit'])