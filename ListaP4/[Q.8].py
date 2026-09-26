V=-1
VotTot=0
M=0
Emp=[]
Vot={1:0,2:0,3:0,4:0}
Por={}
while V!=0:
    V=int(input("Digite Seu Voto\n(1) Para Jonh\n(2) Para Joel\n(3) Para Jeremias\n(4) Para Jacob\n(0) Finaliza A Contagem\n=>"))
    if V in Vot:
        Vot[V]+=1
    elif V!=0:
        print("Código Não Encontrado")
for i in Vot:
    VotTot+=Vot[i]
    if Vot[i]>=M:
        M=Vot[i]
for i in Vot:
    if Vot[i]==M:
        Emp.append(i)
    Por[i]=(Vot[i]/VotTot)*100
print("Porcetagem De Votos\nJohn\n=>",round(Por[1],2),"\nJoel\n=>",round(Por[2],2),"\nJeremias\n=>",round(Por[3],2),"\nJacob\n=>",round(Por[4],2))
if len(Emp)==1:
    print("Còdigo do Ganhador\n=>",Emp[0])
else:
    print("Candidatos Empatados\n=>",Emp)