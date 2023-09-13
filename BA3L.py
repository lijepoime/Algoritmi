from google.colab import drive
drive.mount('/content/drive')

# 3 L
f = open("/content/rosalind_ba3l (1).txt", "r")
patterns = f.read().splitlines()
k = 50
d = 200

st = patterns[0][:k]
for p in patterns:
    if(p != patterns[0]):
        st += p[k - 1]

for i in range(k + d):
    st += patterns[len(patterns) - (k + d) + i][-1]

print(st)
