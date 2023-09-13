text="GCAGGCATTTGGCAAAAAGCGACAACTTCTGGCAAAAAGGCAGGCATTCCATGCCGCCATGCCGGCAGGCATTGCACCCGTTTCGACAACTTCGCACCCGTTTCGACAACTTCTGGCAAAAAGCCATGCCGCCATGCCGCGACAACTTCGCACCCGTTTGCAGGCATTCCATGCCGTGGCAAAAAGCGACAACTTCCGACAACTTCCGACAACTTCGCACCCGTTTTGGCAAAAAGGCAGGCATTGCACCCGTTTGCACCCGTTTTGGCAAAAAGTGGCAAAAAGGCACCCGTTTGCAGGCATTTGGCAAAAAGCGACAACTTCTGGCAAAAAGGCAGGCATTGCAGGCATTGCACCCGTTTCCATGCCGGCAGGCATTCGACAACTTCTGGCAAAAAGGCAGGCATTGCAGGCATTGCAGGCATTCCATGCCGCCATGCCGCGACAACTTCCGACAACTTCCGACAACTTCTGGCAAAAAGCCATGCCGGCAGGCATTCCATGCCGCGACAACTTCTGGCAAAAAGCCATGCCGTGGCAAAAAGGCACCCGTTTCGACAACTTCCCATGCCGTGGCAAAAAGGCAGGCATTCGACAACTTCTGGCAAAAAGGCAGGCATTGCACCCGTTTGCAGGCATTGCACCCGTTTCGACAACTTCTGGCAAAAAGGCAGGCATTGCAGGCATTGCACCCGTTTGCACCCGTTTCGACAACTTCCGACAACTTCTGGCAAAAAGGCACCCGTTTCCATGCCGGCAGGCATTCCATGCCGCCATGCCGGCAGGCATTGCACCCGTTTGCAGGCATTGCAGGCATTCCATGCCGCCATGCCGTGGCAAAAAGGCACCCGTTTTGGCAAAAAGCGACAACTTCCGACAACTTCTGGCAAAAAGCGACAACTTCCGACAACTTCGCAGGCATTCGACAACTTC"
k=5
d=2
def lts(lista):
  rijec=""
  for i in lista:
    rijec+=i
  return rijec
def razlika(r1,r2):
  br=0
  for i in range(len(r1)):
    if(r1[i]!=r2[i]):
      br+=1
  return br
skupsvih=[] # skup svih kmerova koji su blizu kmeru iz teksta
for i in range(len(text)-k+1):
  if(list(text[i:i+k]) not in skupsvih):
    skupsvih.append(list(text[i:i+k]))



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
  skupsvih=dodajsusjede(skupsvih,k)
stringsvih=[]
for i in range(len(skupsvih)):
  rijec=""
  for j in range(len(skupsvih[i])):
    rijec+=skupsvih[i][j]
  stringsvih.append(rijec)
brojss=[]
for rijec in stringsvih:
  broj=0
  for i in range(len(text)-k+1):
    if(razlika(rijec,text[i:i+k])<=d):
      broj+=1
  brojss.append(broj)
print(stringsvih)
print(brojss)
a=max(brojss)
for i in range(len(stringsvih)):
  if(brojss[i]==a):
    print(stringsvih[i],end=" ")
