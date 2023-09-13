# 1 N
skupsvih=[]
pattern=""
d=2
a=list(pattern)
skupsvih.append(a)
def lts(lista):
  rijec=""
  for i in lista:
    rijec+=i
  return rijec
def dodajsusjede(skupsvih,k):
  orig=skupsvih.copy()
  for i in range(len(orig)):
    for j in range(k):
      b=orig[i].copy()
      b[j]="A"
      if(b not in orig and b not in skupsvih):
        skupsvih.append(b)
      b=orig[i].copy()
      b[j]="C"
      if(b not in orig and b not in skupsvih):
        skupsvih.append(b)
      b=orig[i].copy()
      b[j]="G"
      if(b not in orig and b not in skupsvih):
        skupsvih.append(b)
      b=orig[i].copy()
      b[j]="T"
      if(b not in orig and b not in skupsvih):
        skupsvih.append(b)
      b=orig[i].copy()
  return skupsvih
for i in range(d):
  skupsvih=dodajsusjede(skupsvih,len(pattern))
print(skupsvih)
stringsvih=[]
for i in range(len(skupsvih)):
  rijec=""
  for j in range(len(skupsvih[i])):
    rijec+=skupsvih[i][j]
  stringsvih.append(rijec)

for i in range(len(stringsvih)):
  print(stringsvih[i])
