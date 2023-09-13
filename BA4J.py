# 4 J
aminoMass = {
        'G': 57,
        'A': 71,
        'S': 87,
        'P': 97,
        'V': 99,
        'T': 101,
        'C': 103,
        'I': 113,
        'L': 113,
        'N': 114,
        'D': 115,
        'K': 128,
        'Q': 128,
        'E': 129,
        'M': 131,
        'H': 137,
        'F': 147,
        'R': 156,
        'Y': 163,
        'W': 186
    }
peptide="IWAINDCWVKQAWGQYYHYSWIFFNVECCSIWDGCDLHSYV"
lista=[""]
k=len(peptide)
for i in range(k):
  for j in range(i,k):
    lista.append(peptide[i:j+1])
lista2=[]
def zbroj(rijec):
  a=0
  for i in rijec:
    a+=aminoMass[i]
  return a
for i in lista:
  lista2.append(zbroj(i))
lista2.sort()
for i in lista2:
  print(i,end=" ")
