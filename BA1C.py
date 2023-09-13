pattern="ACTG"
def revcom(pattern):
  rj=""
  for i in range(len(pattern)-1,-1,-1):
    if(pattern[i]=="A"):
      rj+="T"
    elif(pattern[i]=="C"):
      rj+="G"
    elif(pattern[i]=="G"):
      rj+="C"
    elif(pattern[i]=="T"):
      rj+="A"
  return rj

print(revcom(pattern))
