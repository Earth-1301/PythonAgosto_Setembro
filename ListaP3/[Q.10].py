Alu={}
for i in range(5):
    Nom=str(input("Escreva O Nome Do Aluno\n=>"))
    Not=[int(input("Escreva A Primeira Nota\n=>")),int(input("Escreva A Segunda Nota\n=>"))]
    Alu[Nom]=Not
for i in Alu:
    M=(Alu[i][0]+Alu[i][1])/2
    print("Nome\n=>",i,"\nMédia\n=>",M)