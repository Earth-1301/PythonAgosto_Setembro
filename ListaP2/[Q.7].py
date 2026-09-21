N=int(input("Digite um Número Positivo\n=>"))
R=[100,50,20,10,5,2,1]
T=[]
for i in R:
    T.append(N//i)
    N=N%i
print("Notas de 100\n=>",T[0],"\nNotas de 50\n=>",T[1],"\nNotas de 20\n=>",T[2],"\nNotas de 10\n=>",T[3],"\nNotas de 5\n=>",T[4],"\nNotas de 2\n=>",T[5],"\nNotas de 1\n=>",T[6],)