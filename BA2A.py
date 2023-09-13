def rosalindprint(res,newline=False):
    text = ""
    sep=""
    if newline:
        sep="\n"
    for i in res:
        text = text + str(i)+sep
    return(text.strip())

def kmer(text, i, k):
    return text[i:(i+k)]

def razlika(p, q):
    if len(p) != len(q):
        return -1
    dist = 0
    for first, second in zip(p, q):
        if first != second:
            dist = dist + 1
    return dist

def kmersfrequency(text, k):
    D = dict()
    for i in range(0, len(text) - k + 1):
        tmp = kmer(text, i, k)
        try:
            D[tmp] = D[tmp] + 1
        except KeyError:
            D[tmp] = 1
    return(D)

def ApproximatePatternCount(text,pattern,d):
    count=0
    for i in range (0,len(text)-len(pattern)+1):
        pattern2=kmer(text,i,len(pattern))
        if (razlika(pattern,pattern2)<=d):
            count=count+1
    return count

def suffix(pattern):
    return pattern[1:]

def susjedi(pattern,d):
    nucleotides={'A','C','G','T'}
    if d==0:
        return {pattern}
    if len(pattern)==1:
        return nucleotides
    neighborhood=set()
    suffixNeighbors=susjedi(suffix(pattern),d)
    for x in suffixNeighbors:
        if (razlika(suffix(pattern),x)<d):
            for n in nucleotides:
                neighborhood.add(n+x)
        else:
            neighborhood.add(pattern[0]+x)
    return neighborhood

def Lwindows(text,L):
    windows=list()
    for i in range (0,len(text)-L+1):
        windows.append(kmer(text,i,L))
    return windows

def kmerswithapproxcount(text,k,d):
    D=dict()
    for window in Lwindows(text,k):
        for pattern in susjedi(window,d):
            D[pattern]=ApproximatePatternCount(text,pattern,d)
    return D

def MotifEnumeration(dnalist,k,d):
    L=list()
    for dna in dnalist:
        L.append(kmerswithapproxcount(dna,k,d))
    RES=dict()
    for D in L:
        for k in D.keys():
            try:
                RES[k]=RES[k]+1
            except KeyError:
                RES[k]=1
    return [k for k,v in RES.items() if v==len(dnalist)]

if __name__ == '__main__':

    x = '''3 1
ATTTGGC
TGCCTTA
CGGTATC
GAAAATT'''
    inlines=x.split()
    k=int(inlines[0])
    d=int(inlines[1])
    L=list()
    for i in range(2,len(inlines)):
        L.append(inlines[i])
    res=MotifEnumeration(L,k,d)
    print(" ".join(res))

    x = '''5 2
TCTGAGCTTGCGTTATTTTTAGACC
GTTTGACGGGAACCCGACGCCTATA
TTTTAGATTTCCTCAGTCCACTATA
CTTACAATTTCGTTATTTATCTAAT
CAGTAGGAATAGCCACTTTGTTGTA
AAATCCATTAAGGAAAGACGACCGT'''
    inlines=x.split()
    k=int(inlines[0])
    d=int(inlines[1])
    L=list()
    for i in range(2,len(inlines)):
        L.append(inlines[i])
    res=MotifEnumeration(L,k,d)
    print(" ".join(res))

    x = '''5 1
CGAAGGGTTCTGCTGTTAACCATCC
TCGAATGCTCCATCAATTTTCAGGG
GCGAGGACCGCATCGACAGCCATTG
GGTACCATCGTCGTTGCAGACGCAA
ATTAAGTGTTAAGGATCAACCATCA
GGATCGGCACACACACATCCTCACA
TTACAACCGTCATCTGCTAGATTCG
TTCTGCATCTAATCAGAGCATATCA
CATCACATAAAATAAAAAGTGCGTA
AAAGCAGTGGAGACACATCCTGCAG'''
    inlines=x.split()
    k=int(inlines[0])
    d=int(inlines[1])
    L=list()
    for i in range(2,len(inlines)):
        L.append(inlines[i])
    res=MotifEnumeration(L,k,d)
    print(" ".join(res))
