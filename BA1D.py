# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OeExzPMoFRfTixKE6s_MdEOW2qtPbz_z
"""

Pattern = ""
Text = ""

def Occurrence(text, pattern):
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern:
            print(i, end=" ")

Occurrence(Text, Pattern)