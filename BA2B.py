DNA=[
"TTCCGAAACATCGGTGCAGTAATCCCAAATTGACGTAAGAGG",
"CCGCGGCTCGCGGTTTACAACTCGAACTTCCCATGCTGGGCA",
"CTCCACTTGGCAAACCTCGTACTACCGAATGTTCTTGACTAG",
"ATACTGCAGGCGCTGTGTCGTTGCTAAGTCCCGGCGAACTTC",
"TAGGCGCCAATAAACTTCAGACATTATCTTCCGAACGGTGCA",
"AGGAGCAATCACCCTCCAGAACAGGCGCGGAACGTCGGGGAC",
"GAGGCGGCTAGGCGAGATCGTGACTGGTAAAACTTCGTAATT",
"AACATCACTAAAGGGTCCCGACAAACCATTGATGCCTGCATC",
"CTGTCTGAGGATCATGCCAGTGCAAGTTCCAACCTCTTCTTC",
"GTAAACAATACTAGACGTGGAGTTGGTCTTAACCTCCGAGCC"
]
k=6
#skup svih kmerova duljine 5
skupk=[]
def razlika(r1,r2):
  br=0
  for i in range(len(r1)):
    if(r1[i]!=r2[i]):
      br+=1
  return br
def permutacije(arr,text,k):
  if(k==0):
    arr.append(text)
    return arr
  permutacije(arr,text+"T",k-1)
  permutacije(arr,text+"G",k-1)
  permutacije(arr,text+"A",k-1)
  permutacije(arr,text+"C",k-1)
  return arr
p=permutacije([],"",k)
def mindistu1(text,pattern): #kmerovi u jednon dnau
  k=len(pattern)
  min=len(pattern)
  for i in range(len(text)-k+1):
    if(razlika(pattern,text[i:i+k])<min):
      min=razlika(pattern,text[i:i+k])
  return min
def mindistusve(DNA,pattern):
  sum=0
  for i in range(len(DNA)):
      sum+=mindistu1(DNA[i],pattern)
  return sum
lista=[]
for i in p:
  lista.append(mindistusve(DNA,i))
print(lista)
a=min(lista)
print(a)
k=[]
for i in range(len(lista)):
  if(lista[i]==a):
    k.append(p[i])
for i in k:
  print(i,end=" ")
