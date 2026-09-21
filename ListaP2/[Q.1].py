N = int(input("Horas estacionadas: "))
if N<=2:
    V = 8
elif N<=5:
    V = 8 + (3*(N-2))
else:
    V = 17 + (2*(N-5))
print("O valor total a pagar é ",V," Reais")
#Esse código usa "if" e "elif" para fazer calculos diferentes de acordo com o número de horas definido por N
#Dependo do valor de N, o código calcula de forma diferente de acordo com os dados da questão