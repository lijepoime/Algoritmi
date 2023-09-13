pattern="ATACAAACGCTTCTTGATGCCCCACTGGG"

def ptn(pattern):
  k=len(pattern)
  n=0
  lista=list(pattern)
  for i in range(k):
    if(lista[i]=="C"):
      n+=4**(k-i-1)
    elif(lista[i]=="G"):
      n+=2*4**(k-i-1)
    elif(lista[i]=="T"):
      n+=3*4**(k-i-1)


  return n

print(ptn(pattern))
