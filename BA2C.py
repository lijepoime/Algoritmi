text="TTGTCATATTCCGATGAGTGTTACTGGTGTCAGTGTGCTTTTAGGCTTTCCCATGGGTGGCCACCTCCTCACAATTAATACAGAAAAGCTGCACGGCTGCGGCGCGGCCTTGACCAGAGCGTTGTTACGGGATTTCCAACGGCGTTTTCCGGGTGTAGTCAGTTGTGATTCAGACTACCCGCCCACGCTAGGCTCGTGGA"
k=8
strprofila=[0.36,0.32, 0.16, 0.28, 0.48, 0.16, 0.36, 0.32,
0.2, 0.24, 0.2, 0.16, 0.12, 0.28, 0.2, 0.16,
0.08, 0.16, 0.28, 0.2, 0.24, 0.28, 0.2, 0.24,
0.36, 0.28, 0.36, 0.36, 0.16, 0.28, 0.24, 0.28]
Profile=[]
for i in range(len(strprofila)//4):
  Profile.append([strprofila[i],strprofila[len(strprofila)//4+i],strprofila[2*len(strprofila)//4+i],strprofila[3*len(strprofila)//4+i]])
print(Profile)
lista=[]
for i in range(len(text)-k+1):
  lista.append(text[i:i+k])
print(lista)
def sansa(rijec):
  p=1
  for i in range(len(rijec)):
    if(rijec[i]=="A"):
      p*=Profile[i][0]
    elif(rijec[i]=="C"):
      p*=Profile[i][1]
    elif(rijec[i]=="G"):
      p*=Profile[i][2]
    elif(rijec[i]=="T"):
      p*=Profile[i][3]

  return p
lista2=[]
for i in lista:
  lista2.append(sansa(i))
a=max(lista2)
print(a)
for i in range(len(lista)):
  if(lista2[i]==a):
    print(lista[i])
