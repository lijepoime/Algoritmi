from google.colab import drive
drive.mount('/content/drive')

# 4 C
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
def broj(rijec):
  sum=0
  for i in range(len(rijec)):
    sum+=aminoMass[rijec[i]]
  return sum
rijec="AKLMQVYSFPCPQYA"
r2=rijec+rijec
rjesenje=[]
slova=[]
for i in range(len(rijec)):
  for k in range(1,len(rijec)):
    slova.append(r2[i:i+k])
slova.append(rijec)
slova.append("")
print(slova)
for i in slova:
  rjesenje.append(broj(i))
rjesenje.sort()
for i in rjesenje:
  print(i,end=" ")
