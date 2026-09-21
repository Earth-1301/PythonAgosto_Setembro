S = 500
for i in range(8):
    O = int(input("Escreva a Operação \n 1 para Depósito \n 2 para Saque\n=>"))
    while O<1 or O>2:
        O=int(input("Tente de Novo \n1 para Depósito \n2 para Saque\n=>"))
    if O == 1:
        N=int(input("Escreva o Valor do Depósito\n=>"))
        S=S+N
        del(N)
    elif O==2:
        N=int(input("Escreva o Valor do Saque\n=>"))
        if S-N<0:
            print("Saldo Insuficiente")
        else:
            S=S-N
            del(N)        
print("Saldo Restante\n=>",S)
