# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LTW7X_XPIBhYMfys4Hr6sSy3w0aJ1KV5
"""

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
#sada smo nalijepili sve iz prvog člana para, sada moramo one iz drugog pri kraju

for i in range(k + d):
    st += patterns[len(patterns) - (k + d) + i][-1]

print(st)