Row="AAGGAGATTGTGGCACGTCGGCATGCCTGCACGTGTCACGACAATAGGACCACCTAGATGAAAGATATTTGATCATATGTGCACACGTGTTCCCTCA GGGCCCCGAGCGCTTTTGAATCACGCGGTAGGCATAGGAATTTCGAGCGGCCACGCATACCGCAGAGGCATCGCCCGTGCATCAATCGGGAGGGGGA CAGGTATCCACTGTGCGGAACTGGGGTGTAAGAGCGATTCATACGCAAACCTAATAGATTGGAGTTTGATCGTCCGACAGTATTCTAGGGATGCTAT ATAAATTGTGCGCAGTACCTGCAGCGTTCTGACCCAACCGGTATAAATAGCGCATCGGTATTACGGTTCAAGTCTGTAGATCGACTGACAACACCGA GCAGGCGACCCGTATTTTAGGCACGAACGCTTTATGATTGTCCTAAAAAGGATGTAGGGGTAGGTCTTACAACTATGATGGGATTAGCAGTATAAGC GCGGCGCATGTCGAGGGCGAAGTTCCGAGCGACTGCACCATGGAGATACTCGATGTTCTTCCGGCGAGACAGCCTAACTGTTAAGACGTCCCTGAGG CAGACCCCGCAACCTCTTATACTTCATTAGGAGGCATTACTTGAGAGAAATCTTCCGGATTGTAAATTAGGAATCACATAAGCCCGTAAATTTGACT CGGAATGAGAAACTTATGCTCGCCGCCTTTGTCGTATATTGTTTATGTTCGGCGTATACCATGGAAAACATTGGTGACACTAGCCTTCCCTACCCGT GTCAGGAAGGGACTGCCGTCTACCTGACTCTGCCGCAGCTGGCAGGTCCTCCTTTTGTTGCAGCTGTTACTGGTTATATTCAAAACCATTTTCAGCA CTTAACCTTGGTTCCGGCAATTCTCACAAGTGGGCACCTGCGGGTGAGGCATAAATTTGGGGGTAACGTGATTTCGCCATGAGAGCAATATTAAAGT CTTTGTCTTGGTTGAATGCGAATTAAACAAGGTCGCGTACCCCGTACTTGTGGTAGGAGGGCGACGCCGCGACGTCCCGGTGGAGTTTGGGACCCGT CCATTGTTAACACCACACTAGTTTCCACGCCTTCTCCGCCTTTACAGCGCGTCCTATATTATTAGCATGCCCAAAACGTAGTGCAAGAGCAGTTCCG TCGCCCAGGTTCCCGTTGAGGGTGGAAAATGGATCACACGGTTTTCACACTGTATCCTAGGGTATTTGTGCTGTTCGCGACCTCCGGCACCCTACCT GGCCGTGGTAGTTTAAGCCTATGCTTGTGATTATAAGTAGTATGACCAGACGTTAATGCGTGTTCTGGCAGAGCAACCACTCTTTATCCTCTTGAAG ACGTTTTGTGGACCTCCTCCCTCGTCCATCCAGAACCAATGTCAACTTCGCGGAGCGTGAGGTATTCATGTGTGGAGTGAACCCGGTGGCACAGCGC TTGACCTATTGGGCGGGCAGATGTGAATGTCGAGGTCAGCGTTTGCAAAAACTCAGTCTCCGAGTCCCTCGAAAGTGGCGAGAGATTGTACTCACAC TCATTCCCATGTGCATCTCGCTTGCGCATGGTGGTGCAGGGGCCTGTCCAAGACCCAAGTTCAGATTTCACGAAGCGGAATGATCAACAAAAAGGCC GGGTGTCCGCCGGAAGAGCCGGGATGTTTGAGGAGTGGCTGATTTCCTAACTTGGGGTGACTGTTGCATCTGTTCCGAATTTCCAAGTCCTCGTGAA GGCGATAATAGTGTCCATACCGCGAGGCTTCGGTAGTGATGGACCTCAATGATTCGGGACCTACCTCACAGCTCTCCCGCCAAAGCTCCTTCACGCA GTAGGGAGGTACTGTGGCATGATCAGGAGTTCTTCTAACCAGTATACGCCCCTTGGGATCAATGGTCTCATGGTTGGGGAGAGGAGTGCTAATAAGA CTCATCGTACCTTGCGAGGGTCATATGCCGACCCCATCTGAATGTTCCGCGGCATGTTGCAATATGCCGGAACCTGTTTTGGCTCATCAATGTTTTA AAGAACTCAGGACGTATGATACTGACTATCACGCACGGGGCCACTGTTCATAGAAATGGTGAAGACTCTAATAGCTAAGTTCCCTGGTTCAAAAGTA AACACGTGTGTTCATTGGTATGAAGGGGCGACAGTCTTAGTGCCAGCGTTTATGAGACAACGGTTGTGATAGAAGTCCTATTTACGCGATGGCACCA CCGAGGAACTAATCCGCCCCTCATTGCCGGTTTGTTTTGCCTCGAGTGGACTCCCGATATTAGCTGTAGTATATCCTCAGATCTGTGCACCTGAACT CTGTGCTCGGTAGTTCGGTTCTAGGAGCCACTTGCCACCATGTTTTTTGCTTATTCTAGTGTGGTTCCTATTTCCTTCAATCCATTTGTAATCTGTT ACGTCTCTGTGTAAGGCCTGTCGCACCAAATGCTCAATTAACGGAATCTGGGACTCCACTGCTCGCCGTATGGCCCTCGTTGTTGAGGCTAGTAACC CTTCGTCGCCGTACTATAACCAATATAGCAGTTTAGTTCGATCTCACACGACCCCCCGACTCTTATCGAGACGGCGGTTGTGGGGCGCATGCGGTAG AACCTTAAGATCCTGTTTGAAAAGGCCATACTCGGTGCCCAGAGTAATAGCAGTGCAAGTTCTGCTTGGGAAGCGATATTCGCGACGTATGTTTTCG TTCATTTACTCGAAATCCCAGTTCCGCTCGCGAATTCGGCACTTGTTGGCAGTTGTGAAATACTGAGAACGGTAGCACGTGCCGACCGGCAGTCGGG GACATCTACACAGGTTCGTGGGTGACTTTGATATATATCCTAGGTACACTATATACCCCTTGGGATCTCCCACATCCGTAGTCCTGCTAGAGGCAGT ACGTGTAGGCAACAGCCCGAGGCTCCCTGTTTGTTTGATTTTGGGATATTGAGCAATCAAAATTTATTCGCCAATCAAAGCGATATGTCTTCCGCAC CACACTCCTCTTACACCAACCGAAAGCAGGATTGTCCATTCAAAGTCTGTCACGCGCATGCTAAGCGGCTTTTACGATGAAGGTTAGGGGTCCTGGA AGTATATGTTCACTCCGTTCTGGCGGACCAGCGGCTCCCTAACTAGCAGGCCCGCCCCGGTCCGTCAGCTAGCTCCTTCCCGCGCGGAACGAATCGG"
DNA = Row.split()
pattern="TTGGTT"

def razlika(r1,r2):
  br=0
  for i in range(len(r1)):
    if(r1[i]!=r2[i]):
      br+=1
  return br
sum=0
def mindistu1(text,pattern): #kmerovi u jednon dnau
  k=len(pattern)
  min=len(pattern)
  for i in range(len(text)-k+1):
    if(razlika(pattern,text[i:i+k])<min):
      min=razlika(pattern,text[i:i+k])
  return min
def mindistusve(DNA,pattern):
  sum=0
  for i in range(len(DNA)):
      sum+=mindistu1(DNA[i],pattern)
  return sum
print(mindistusve(DNA,pattern))
