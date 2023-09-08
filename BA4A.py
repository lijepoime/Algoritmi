# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LTW7X_XPIBhYMfys4Hr6sSy3w0aJ1KV5
"""

from google.colab import drive
drive.mount('/content/drive')

tablica = {
        "AAA": "K",
        "AAC": "N",
        "AAG": "K",
        "AAU": "N",
        "ACA": "T",
        "ACC": "T",
        "ACG": "T",
        "ACU": "T",
        "AGA": "R",
        "AGC": "S",
        "AGG": "R",
        "AGU": "S",
        "AUA": "I",
        "AUC": "I",
        "AUG": "M",
        "AUU": "I",
        "CAA": "Q",
        "CAC": "H",
        "CAG": "Q",
        "CAU": "H",
        "CCA": "P",
        "CCC": "P",
        "CCG": "P",
        "CCU": "P",
        "CGA": "R",
        "CGC": "R",
        "CGG": "R",
        "CGU": "R",
        "CUA": "L",
        "CUC": "L",
        "CUG": "L",
        "CUU": "L",
        "GAA": "E",
        "GAC": "D",
        "GAG": "E",
        "GAU": "D",
        "GCA": "A",
        "GCC": "A",
        "GCG": "A",
        "GCU": "A",
        "GGA": "G",
        "GGC": "G",
        "GGG": "G",
        "GGU": "G",
        "GUA": "V",
        "GUC": "V",
        "GUG": "V",
        "GUU": "V",
        "UAA": "*",
        "UAC": "Y",
        "UAG": "*",
        "UAU": "Y",
        "UCA": "S",
        "UCC": "S",
        "UCG": "S",
        "UCU": "S",
        "UGA": "*",
        "UGC": "C",
        "UGG": "W",
        "UGU": "C",
        "UUA": "L",
        "UUC": "F",
        "UUG": "L",
        "UUU": "F",
    }
rna="AUGUACAUAUUCAAAAAGGUUCUCUCUUACACCAUCUCCAGCAAAAGCCAAUUUUGUUCUAACACGUGGUUAUGGCUCACGUCCUACUGGUAUUCAAGUCUGGGUUUACCAGUCGCCGAAGGCACCAUUCCCGCCACGAUCACCCCGGUAGUCGUCUUUUCGAAGUUCAUCGAGAGGCUCGAAUACUUCGAAUAUCUUUUCAUCAGGACAGUAAGCCCAGCCUCGUUAGUAUCGGUAGGAGUUAGAUCUCAAUGGAGGAAGCGUGCGACAAUUAUCUCAACGAUGGUUUUCAGGUGUCCAGCACUUUUUUUAUAUAGGCUGCGCUUACCGGGAAUUCACAUUUCAUCUGGAUGGAUGCUCCUCGGGUAUACCCCAUCGUCGUACGGGCCAACGUUAGCUGGUCAUCAAGUCACUGAGCAGCUCAGACAGUGGCUAUGGAGACAAACAGCACCCCGAUUAAGCUGCUUUAUUCUCCAGGUCAAUGCGGGGGGUACCUGCCAGGGGAACUUUGCGUUCAGGGUUACGAUUGGUGCUUCAAGGGUUUGGAACGAUACAAACAUGCCACCACAACACUGUAACCGUUGGACUCCUCUAUUUAUAGUUUGCCCUACGACAGCUGCGCAACGACGAAGGGUGUCUAACCUAUGCCAGCACCGUUGGUCACUAUUUUUGGGCCCGAAGGGGAACCCCGCUAAGAAGAGGCGACGUAAGGAAUGCGUGAUCGGAAUGCGGCGCCGGUACUCUGCUUCACCUCGCCUCUUGUGUUGCGACCGAAAGAGCGGCAUCAGGCGUAGAAAGUGGACCGAUGUCCCGGAAAAACACAGAGAUAACUGCAGGGAAAUACAUAUUAGGCGCAUCACUAAAAUGGAUCGGGUAAUGACGGGCAAGCUACGACGGAACUUCGAUAUCUUGCUACCGGUCAUCGGUGGCAGCCACUCUAAAUCAAGCAGUUUCAAAUUGCCCUUGAUUUCUGAAAUACAUGCUGGUCAUUGUAUCGUGCUUUUAGUGGAUAGACCACCCAGGGUACCCAAAAAGCCUCUUCUAGCAACGUCUACGGUUAUGGUGACCACUGUAACUAGGGUGCUGUGGAAUUCCGUGCACACAUGGCUCCACGCGGCCUUAUCGACUCAGUUCCUCCUUGCGGAGUGUUACAAUAAACGGAAAGUGCUGGGGCCCCGUCCUACACAUACGAAGGGGAGCUUGCACGGUAACCGAAAAGCAGAUGGAUGGUGGGUCGCAUGGAUGAAUAGCCCUCAGAGCGGCUUGAGAACAAAGGCGAUUCCGCACUCUGAACGCCAAUACUAUAGAGUAGACACCCACAUGAGCUGGCAAUGGUUAGUUGACCACGCUUAUAGUGAAACGCGUUGCGGAGCUUGUGGAGUCACUCGAAUUUUCGUGUAUAAUGGCUUCUUAUACAGCACGGGUUUUGAGACGGCCCCGGGAAGCUUAUGGGAUGGGACAUCUGCACAGGUCUCGCAGGGAGCAUUGAAGACGACGCACUGCCCAACCGUGAAAACCUCUUCGCGGGUGAACACUAACAUGGCCGACCUCCAUCCAUGGGAGGCCCAAGUAGCAAACCUUCAGCACACCGCGACCUUUUUCCCAAAUAACACAAUGCGUCAUACAAGUUCUCAGGGAUUAACGGCCUGUGCCGAGAGCCCUAAUGUUGGCGCGUCUGUGUACUCUUUCGACGGACUCAGACGAUCAAUGGGACCGGUCUGCGACCCAAUUAAACGAUCCCCGAAGAGGGACUUGAUUUGCCUAAGGCGCGUUGAAACGGAGAUGAACCCGCAAUGUUACGGCACAAGCCAAGCGCGAAACCUCGGCUACCUCACGGUCACUAUAUUAAUAAAGACCUUAGCAAGUAGUUUCGAGGUAUCCCCGGAUGAUUCAUCUUGGCGGUCGGGCCCAUCCCGAGAUUAUACACGGCAGGACGGAUUUAAUCGGGGUCAAAUUAAGCCGAAGCAUACGACAGAGACAUAUGCGAAUUGUACCCGUCUACCAUGUCAUAGAGAGUUAGCGGCGACAUAUCAGCCCGGAAAUCGCCCGGCCAUGCUAAGUUAUAGUGACCUACUUGUUCGAUCACUAUCCUCCGUAACCGGGUUGGAAUCCUUCCGGAAAUGUGGCUGGCCUUCAUCUGUAGGUAUAAAGACGGCUAUAGGUUUUAAACCUCCCCGCACGAUCUGUUGGGCGCUAUCUGAAAUGACCCCUCUAAUCUUUUCUAGAGUGGUCUCAUCUUCGUGUCUCUUCCGCGCGCUCCAAGCUGACGGGAAAACCAUAAGCACUCAUCUAGAUCACCCGUACCCUCUGCACUGCACUUCGCGUCAAUACUUAGUACCCCCACUGUCUUUACGAGGUACUGCUUAUCUUUGGACACUGGUCACGGGGGCACGAGACUUGGCGAUAUAUGCAAGUUCUCAAGUUAUGCCACUGCCAGUUAUGAAGUCUCUCGACCAAGAAAGGAGGUUGUUGCUCCAGCAGGAAGAUGAAUCAUACCCGCAGAGUUUUACGGAAGCAAGCACCUUAAAGUAUUUUGCUCUUCAAAGGACUGGUCGUUUCCGCCGAUCAGUGCACUCUUGGGACACUGCCGUAGUGGUACGGCUCACUCGAACCUGGCGAUGUGCGAAACUCCAUAAACCGAACGCAGAGGCUGCCGUGUGCGCAAGUAUCUCCCGACAUAUUCUUUACAGUCAUGUUACCGGCUCUAGGUUACUACCGCUAAGUGCUUUGUCCCCGUCGCAGAAUGGGCAUGGGCGUGCGAGGUAUAGUGUGACGAGGCAUAGAGAUACUGACCAUCCGUCUCAGGCGGAAGAGCGGGUAUACUAUAGAUGCCCUCAGAGAGGUAUGAUACGCCACACCAGGGUCCAAUCUCUCCUCCUGUUGCAGAAGAUAAGAUGUUUUAAACAACUUUUAGGCGAACCAAGGAGUGACCAUAUAAGGAGUUUUAUCCACUUCCGGCUGCACGUGACGGGCCUGCUUACCUGCACUGUUUGCUCCACAUGCGCGCUGCGGGACCGUAAAGUUACCACACCGCUCCUUAGGGUCGUAGGCAGAAUUAUGCACGGAGGGUCCACAGCUCCUCACCUGGAUAUUUCGAUAGGACAAAAUAGGUCUCGCCGAGCCGCCAGUUGGUGCCGUAGUUGCCGAGGAAGUGCACUGUUUGCGUUUCACCGAUGUAUUAGCCUGCGCCCGUCCAUGUAUGGUUGCGGGUCCAUAGGGCACGGCAAACGCAAAGACUCUAUAUGCCCUAAGCACCAAUCUGUUUCAAUUGAUAGGGCGCACAACUACAGUUACGCCCGGGCGAUAAGUCGAAUCUCUUAUCGUUGUAGUUUACUUGUAGAAUACACCGUGACUCUAUCGUUAUUGCGGACACACAAAGACGUUGCGGUGAUAAUAGAUCAGGCAAGCUCCCGGAGCCAGUACCCUCAACUAGUCAAGGAUCGAACGGCUGCGGAUGCAGGGGCCCACUUCUUCUUCCGAAAAACAUAUGAACGGUACUACGUGGCCCGGGAUAGUUUUGGUCUACUUCUAGAGCAAGCGCACUGUCGCAGGUGCUAUGUAGUCGGAUACGCAUUCCCCCGACCCCCCCGAUGUAUAGGUAACAUCGAAUGGGAUAUACAGCGACGUUGUUACUUCCGUUCUCAAGGUAAUUUGAUCAAUCUUGUUCUUGCGUUACGUAUCAUGCCUAAUUUGAUCGUCUGGCAAAGGAGUCGACGUGAAAAGCUGUCACCGUAUAACGGUAAUGAAUGCGGCGCAUUUGGCCCCGGAUGCAUUGGGUUAAGGCUAGUUCGUCGACAGGCCAGGUAUGUUCGGCAGGACCACGUAGUCCAAAGGGGUCGGUGUAAAAUCGCGUCGUACGGUGUGGUGAGGCGCAAACAAGAGCGCGUCAAUAGCAGUGAUGCUAGGCCUUCUAUGUUGAGCCAUAACUUUGGCCCUUCGGUUCUUCGCACCGCCGCAGAACUGAUACCGUGUGUGCGACAACAUGGUCUUUCGGCCUGUCGAGCCGUUAUCAAGAAGACUUUCGCAGGCCUCUGCUCCACGCACAUCACCUCCGUGAUACGCAGAGUAGAGGAACUUCUCCAAUGGUCAGGUCGUUUGAACAUAACGACACAGGGAGCCCGAAAGAGUAUAAAAACGAGCCCGGCGCUGCGGAGGGGGAAAAUAGUUGCGGCUCGGUGGAUGGCGGUCCCCACUCAUGGGCCCAGAGCAGGACUAACGGUGUUGGCGUAUUCAGACCGGUUCGGCUUUACUUACUUUGACGAACGACGCCGCAUGAAGUGCAGUCGCGCGGCAAGGCCUAGAUUUGUCUCGUCGGUGGCGACAGGCGGUAGAACUCGCGGGCAUGCUACGCGUCGAUCAUCCAAUCUUGGAUAUGUCUCUGUCAACCGCUGCUUGCGGCUGCCCUGCCUUGCGCUUUCAUUCCAUGUGUCUCGCACUUCAGUGGCGGUGAGAGAAUGCGAGGAGUAUGGCUUGUGUGUGCGGAGGUUGCGGCCCCUUUCUCACCCUAGUUGUGGUAAGGUGGGUGAAGUUUUGCGCUGGUACGACUUCGUGCGAGCUUCAGUCACUAAGACUGACCCCGAGUCUAUCAGAAUAACUGAGACGCCCCCUGUGGGCGUAUUGUUCUGGUGGUUCACAAGGUCCCACCCAGUAAAGCAAUGCUGGGAUCCUCGCGAUGUGCUGCUCCUUCGUCGACUAUCCAAAGUCUUAUGGGAAGUCGGUAAGGAAAAGGGAGCGGUCGUUAUUAGACCCACGCAGUUUUCGUGGCAUCUGAGGUCUGAUGCCGAUGUUUUCCACUUCCCCCUCCAGCGCUGUUUUCAGAGCGGCGUUCGGUCAGUGGCCAGUCCCCUAACAGGCCGGAUUAGUAAACGCUCCCGACCGCUCUGCAUGCCAGAGCCGGCCGUUUCCAGGUCUAUCCUCCAAGAAGAUAUACAGUCAACCGGAUACAAAAUACUCAGCACAGUCCAUACCGCUUGUGCCUUCUCAGAUCCGGUAAACCAGCAUUGUUGCCGCCCGGGGGCACCGGCACAAGAGCGGGGGCCGCGUAGUUUCAUAACCGUACCAUACGGUCUAAAGAAAGGAACGGCAUCUGUUCUUAAAGUGAGACACCCGUUCAACUUUCUACAGAUACGGGUUUUUCUACAAGGCAGUCUCCUUCGCGCCGAGCCCGACGCGACAUUUAGCGAGCUCUCGGUAGGGUGGAAGUGGUCUUCUUCUCCAUGUACCCGAGACCCUAAUCAUCCCAUGCGCUCACGUCCAUACAGCGCGCACGUGCGGUCAGGCAUUGAGGAGCUAGCCACUGUUCAGACGAGACGUGCGGGACAAGGCGAUCUCUUCCUUUCAUGUCUAAGUCCCGCGCUAAGUAUGCCAUUUCACAGACCGCCUGGCUGCGACCAGCUGACGGCAACCUGCGUAGAGACCUGUGCUGGUGAAAAGGCAUGGGUUGCCGGCACCCUACUUCAAAUCUUCCGAUCUCAUCCCCGCUUAACGGGAGUAAUCCGCCCGCCCCUGCCCGGUGCUAGUUAUAGUUGUCCUCAGAAGACAGCUGGCGACUCAGCACCAGCUGGCAGGGGCCGGAGUCAACCGACCAAACGCAAAUUUCGGAGACGUCGGUGUUCCAACUACGCAUUGACACUCCGAGACAUAAUCCUACGUACGGAUUGGCAAAUCGACAACCCGGCGGAUGGGGCUCUGCUCGCGGUACCACCGCGCAGACAGCUUACACACUCGGCGCCUCGUUGGGUGGGAAGUAGGUUAGGACGACGCCGUUCGUCCCCAUGGACCGUAGUCAUAAUUUACCCAAAAAUCAACCGUGACGUUAGUCUUUUACGCCGGUAUGUCAAGGGAGGCUCAGUGCACAAGUGUCUAGUGCUAGUUAUGCAGGCGAAGCGUUGUAGCUAUUAUGUUCGAUCUAAUUCGGAGAGGUUUACAUCAUUAACUCAAGUUCCUAAAGUAGCGGCUAGUCGGGAUUCUUGUGAGACCGCAACAUCGUUCGUACCGGCCGGGAACAGGUUCGAAGACCAUGCGUCGCGAUACUUUGAUCAAAAAUUUUACUGUGAUUACUUGUCCGGAGCUGACGCGACCAAGUUUGAGGGCAUACCAUACUCGGGGUCGUGGGGGGAAGUGUCACACAUAUCCGGGUCCCCCACUACAUCUACGUACGGCGACCGUUUGUGGGGCGACACAGGUACACUAGAUCCAGACACACGUGCACCAAGGCGCACCUCCAACGUCCUUUUCGAAAGGAGCUCGAGACAAGCGGACCUAAAUCGGUGUAAAGGCGGACCUAUAUUACUAGCUCUCCGCGAGUCGGAUCAAUUUUUGGUUGGUCAGCUUGUAGGGCCUUCUAUGGUUCCGCCUGGUGUUGUUGCCCUAACUCCCGUGGGCCCGUCGAUGCAUGAAAUCACCACUGAACCUCUUAUGCCGUUAUUACCUCCACAAUUUCUCAAACUCUCUCCUCCGGUGUGGAUGACGCCCUUGCUUUCGAGAUAUAAAAACACAAUUGAGCCAACUAUUAGAAGCAACCUGGGCGCUAUUCGCUUUGGAAGACGCGACUGCACCCUUAAACGAGAAUAUGUGCUUGGUAGCGGGUGUAGUCGUGCACCUCAGAUCCAUAGUUACGCAACGCGUUUUCCCGAUCGGAGUCUGACUAAGAACGAUCCUGCGUAUUCCCUUUCUAUCCAACGCUCUCCUCAUAGGUCCCUUAACCCACCGACCGGAGAAGGUACUGAGCCAUUGGGGCCCAUUGCGAGGCUAGCGCAGACUGCCGGCGCCGGGCGUGGCAGCUGUGCAAUGACGAGAGGGUAUCUUAGCGGGGACACCGGGUACUCAGCGUUAGUCUCGGGAUCCACAAAGCCGGGUAUAUGGGCAGAACCGAUGCGGUUUUCUGGUGUCCGCCAGUUCUCUAAAAAACCAGGCCUGGAUGUUGACAGUGGCAAGUACUAUCUGGGGGCUAUAUGUGAGGCUCUUAGUCUUAUUUCCAUCUCGGGGGCCGUUUGCUAUGAGACGUGUCCAUACGGGGUUAUAGUGUUAGCGUUGCGUUGUUACCUUCGGCUCAAGGUGGUUGCACAUGAGGUCGAGCAUCAUGGUGAUGCCUAUGCAGACCGUCUGUCUGUUGUCGCGCCUGUUUUAGUAUCCAAUGGAAACAAUUGGGCCAUGUCUCCGAUUACACGGAGUGCUGAUAGAGUUUCCCCCGUCCGCAAACCGCUCCAAGUGAACAGGAAUGUUGUAUACAGCUCUCCGGGACUACCCUACCUCCCCGUUCUGCACGACGUUCGAGACAUGGGCUACAAACGCCAGUGGAUAUCCCUGGAUGGAGCUGUUGGGAAUUCGUCGUCACAGUCACUUGCAUCCAUCAGGGUCUCCGGACCUUUGGCUCUGAUCGUACAUAUUUCAAUAUGGAAAUCACUGUCCCGGGGUCUACCCACCUCGGCUAGCGAUUUCAUAUCAACCUCACACGGGUCUGACCCAGGGGUAUGCCAGACUGACACUAGUCCGUUGCUAAAGGACAAACAAAAAAUGGGUUCGCCAGGAUUGCCCGGUAGAAUGUGUGGGCUCAAAUUUUGGUUAGUGCCUAAUUGCGUCCGAAUGUGUCUAUCCGCUAUAACAACAUUCACCCUUCUCCUAAAUAAACGUCAGACGAUAAUAAACUUAGCGUGCGCGUGGAUAAUUGGGUACCCCCUCCCAAUGUUCGUCUGUGUAUUACCUAUCCUGACAGGUUUCAAAUUAGGGCCCGGUCGACGCCUUGCACUUUUACUAUCUAGUAGUGGCUCGUUUAUUGAGGUUGAGCGCACGGUGGCACUUUCGCUGAAGUGUGGUUCCCUCUCGUUUGGCGUAGCUGUACAGUGGUGCUAUGAGAAGAUGGCUAAAUCCGCGGAGCCACGAAAUGUGCUGUGCUGUCGAAAGGACCUACUUACGUUCGAGAACAAAAGACAAACACGGGCGUUUUCAACUGAUGUUGCAACCCGUCACAUCUUCGUGCGACUCCGGCAACAGGACAUUCGUGCCGUGUCUGCAAUUGGCGCCGGUUAUUUAGUCUCGGUAACGGUUGACAUGUGCGAGAACUUUAAUUUAGGUCUCUUAUCUACUUAUGGAGGGGACCCACGCCUACGAGUUCAUCUGAUUGCCACCUUGAAAGCGGCUGCAAUCUCCUAUCACAAUGUUGUCGGUCGCGUCAGACACUGUGCCAGUCACCCGGCAGAGGCUGUCCAAGAGAAUCUUUUGCCGAUAGUCAGACCAACAAGUAAGCCACUCAGAGUUUUUGGGAUGCUUGUGUCGCGUCCCGUUAGUCCAGGUCCCGGGAGCCCGAACGUCGCGAGAGCGGUACCCGACGUCUAUGCGAAUCCCGAUGACGAAACAAUAAUUAAGGGCACUCACGGGCGAGGACUGCAGACCUUCGAGUUGUCCAGACUUCCCAAUAUAGAGUGCUUAAGACUGAUGUGGCAAACGACAGCUCGGGUUAUCAGCGAGCCGACUACCACCGAAGACGAUACCUAUAAAGUCGUAUCCGUAACUCCGAUCCUCGUAACCCCGCCGUGGGCACCAGCAGCCGCGCACGGGCCCCCGGACUCACGUAAGUUAGUAAGGCUUCCCGUUCGUGUAGUACGCGAACAACUAAAGGUGGUAUCUCAACGGGCAACGGUUGUUAGAAUAUACAUGCUCAUGCCUGUUGAAGAAGUGCGAAGUGGGAGCCUUCGCCUUACGUAUGGGGCUUCAUUUACUAUUGCAUAUUACGCAGGGUUUAUUUUAGUCAGCCGACGCCGUCAAGUGUGGCCACCCAACUGUUUUCUUUUGCAUGCUCGUAGUGGCCUUUCUUUUGUGGAAGGAGAAGGCGACUGCGUCACGGGAUACUGUAGACUGGCAGCUAAUGGUAAGAGUAACCUGCCUCCUCACAUCCGCAGUUCUGCGAUUUGGCCAUGGAUAUCUAACGUACGUGGCUUUGAAAUAAUAGAGUGGGCGUCGGGUAACCACGUCAGAGUUGUUACCGGUGAUGUAGAUACACCAUCAAACCCAUUACCCCUCGGCUCCCAGCCGAUUCGUAGCAACACCCGAUAUGUUAGUCUACAAAAUAAGUCCUAUGGGCUGCCUGCAAAAGAGACUUCCAGGGGUGUGACAGUUAAAGGGAGGACGUCCGACUUUCUGACUAGUCGUCGUCGGCAGAUCCACAAGCCUGUUAGUAGAGUGGAUACGUUCCUCAGGCAUGGUUUAAGGAUGCACACCGUGUGGGUUUUGAAUCACGGAAACCUAGCUCAUCGGUAUGUAGAAGAUCAGUCAAAGCAGCGACUUUGUCCACCUUCAGGUUUAUCUUCCUCUGCGAGUAACUCGUUGGUCGGACGUGAUAUGCAUCUUUUGGGUAUUUUAACUAAAUGCCGCGGGAAAGCCCAAAGUCGUGGCGAGAACGCCACCGCAACUGCCCAUAGACGUAGUAAUUGUUGGCCGGUCCGGUAG"
rnar=[]
for i in range(0,len(rna),3):
  rnar.append(""+rna[0+i]+rna[1+i]+rna[2+i])
print(rnar)
kod=""
for i in rnar:
  kod+=tablica[i]
print(kod)