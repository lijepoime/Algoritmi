text = "CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC"
k = 5
L = 75
t = 4
#Svi kmer u jednoj L,t
def Count(text, pattern):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern:
            count = count + 1
    return count
skup=[text[i:i+k] for i in range(len(text)-k+1)]
print(skup)
rjesenje=[]
def provjerajednog(text,k,t):
  skup=[text[i:i+k] for i in range(len(text)-k+1)]
  for i in skup:
    if(Count(text,i)>=t and i not in rjesenje):
      rjesenje.append(i)
for i in range(len(text)-L+1):
  provjerajednog(text[i:i+L],k,t)
for i in rjesenje:
  print(i,end=" ")
