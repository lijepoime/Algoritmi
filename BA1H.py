text=""
pattern=""
k=5

def razlika(r1,r2):
  br=0
  for i in range(len(r1)):
    if(r1[i]!=r2[i]):
      br+=1
  return br

def fja(text,pattern,d):
  skup=[]
  for i in range(len(text)-len(pattern)+1):
    if(razlika(pattern,text[i : i+len(pattern)])<=d):
      skup.append(i)

  return skup

lista=fja(text,pattern,k)
for i in range(len(lista)):
  print(lista[i],end=" ")
