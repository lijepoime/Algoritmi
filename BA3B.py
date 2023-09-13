from google.colab import drive
drive.mount('/content/drive')

# 3 B

f = open("/content/rosalind_ba3b (4).txt", "r")
patterns = f.read().splitlines()
print(len(patterns))
patterns=list(patterns)
k=len(patterns[0])
st=patterns[0]
for i in range(1,len(patterns)):
  st+=patterns[i][k-1]
print(st)
