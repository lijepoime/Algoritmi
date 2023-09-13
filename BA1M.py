number=6246
k=7
##   213=3*64+1*16+1*4+1*1
def ptl(n,k):
  list=[]
  for i in range(k):
    a=n//4**(k-1-i)
    list.append(a)
    n=n-a*4**(k-1-i)
  return list
ptl(number,k)

def ListToDNA(list):
  rijec=""
  for i in list:
    if(i==0):
      rijec+="A"
    elif(i==1):
      rijec+="C"
    elif(i==2):
      rijec+="G"
    elif(i==3):
      rijec+="T"

  return rijec

print(ListToDNA(ptl(number,k)))
