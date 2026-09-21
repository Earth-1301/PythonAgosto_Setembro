NSec=37
N=int(input("Escreva um Número\n=>"))
T=1
while T<5 and N!=37:
    if N>NSec:
        N=int(input("Tente um Menor\n=>"))
    if N<NSec:
        N=int(input("Tente um Maior\n=>"))
    T+=1
if T==5:
    print("Pesâmesa! Você Errou. \nErros\n=>",T)
else:
    print("Parabéns! Você Acertou.\nTentativas\n=>",T)