from google.colab import drive
drive.mount('/content/drive')

# 3 B
# 3 C
f = open("/content/rosalind_ba3c.txt", "r")
patterns = f.read().splitlines()
print(len(patterns))
patterns.sort()
print(patterns)
k = len(patterns[0])
for pt in patterns:
    st = pt
    for pt1 in patterns:
        if(st[1 : k] == pt1[0 : k - 1]):
            print(st + " -> " + pt1)
