N=7
X=int(input("Descubra o Número Secreto\n=>"))
T=1
while X!=7:
    if X<7:
        X=int(input(("Tente um Maior\n=>")))
        T=T+1
    elif X>7:
        X=int(input(("Tente um Menor\n=>")))
        T=T+1
print("Parabéns! Você Acertou.\nTentativas\n=>",T)