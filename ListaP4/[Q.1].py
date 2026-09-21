L=[]
for i in range(10):
    L.append(int(input("Escreva Um Número\n=>")))
X=L[0]
Seq=1
SeqAtu=1
for i in L:
    if i-1==X:
        SeqAtu+=1
    else:
        if SeqAtu>Seq:
            Seq=SeqAtu
        SeqAtu=1
    print(SeqAtu)
    X=i
print("Maior Sequência\n=>",Seq)