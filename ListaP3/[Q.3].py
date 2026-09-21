N=["Astro","Bassie","Bobette","Gourdy","Pebble","Shelly","Sprout","Vee"]
L1=[]
L2=[]
I = 'COMEÇO'
while not I == 'FIM':
    I=str(input("Escreva um Nome ou digite 'FIM'\n=>"))
    if not I == 'FIM':
        L1.append(I)
for i in L1:
    if not i in N:
        L2.append(i)
print("Nomes Diferentes:\n=>",L2,"\nNúmero de Nomes Diferentes\n=>",len(L2))