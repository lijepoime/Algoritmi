def Count(text, pattern):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern:
            count = count + 1
    return count
def permutacije(arr,text,k):
  if(k==0):
    arr.append(text)
    return arr
  permutacije(arr,text+"A",k-1)
  permutacije(arr,text+"C",k-1)
  permutacije(arr,text+"G",k-1)
  permutacije(arr,text+"T",k-1)
  return arr

p=permutacije([],"",k)

print(p)
for i in (p):
  print(Count(text,i),end=" ")
