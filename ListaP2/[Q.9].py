D = []
X = 1
N = int(input("Escreva um Número\n=>"))
while X <=N:
 if N%X == 0:
    D.append(X)
 X += 1

else:
    print ("Divisores:\n",D,"\nQuantidade de Divisores\n=>",len(D))