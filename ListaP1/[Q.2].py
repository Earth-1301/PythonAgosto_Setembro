N1=int(input("Escreva a Primeira Nota\n=>"))
N2=int(input("Escreva a Segunda Nota\n=>"))
M=(N1+N2)/2
if M>=7:
    S='Aprovado'
elif M >= 5:
    S='Recuperação'
else:
    S='Reprovado'
print("Média\n=>",M,"\nSituação\n=>",S) 