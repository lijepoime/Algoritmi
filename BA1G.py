a=""
b=""
def razlika(r1,r2):
  br=0
  for i in range(len(r1)):
    if(r1[i]!=r2[i]):
      br+=1
  return br
print(razlika(a,b))
