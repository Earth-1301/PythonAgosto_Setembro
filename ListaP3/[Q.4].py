DS=("Domingo","Segunda","Terça","Quarta","Quinta","Sexta","Sábado")
N=int(input("Escreva um Número de 1 a 7\n=>"))
while N<1 or N>7:
    N=int(input("Tente de Novo\n=>"))
print("O Dia da Semana é ",DS[N-1])