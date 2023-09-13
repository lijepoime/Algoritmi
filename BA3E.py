from google.colab import drive
drive.mount('/content/drive')

# 3 E
f = open("/content/rosalind_ba3e (1).txt", "r")
patterns = f.read().splitlines()
patterns.sort()
dicta={}
for i in patterns:
  dicta[i[0:len(i)-1]]=""
for i in patterns:
  if(dicta[i[0:len(i)-1]]==""):
    dicta[i[0:len(i)-1]]+=i[1:len(i)]
  else:
    dicta[i[0:len(i)-1]]+=","+i[1:len(i)]

mykes=list(dicta.keys())
mykes.sort()
dicta={i:dicta[i] for i in mykes}
for k in dicta.items():
  print(k[0]+" -> "+k[1])
