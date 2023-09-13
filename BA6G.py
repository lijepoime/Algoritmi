from google.colab import drive
drive.mount('/content/drive')

def cycleToChromosome(cycle):
    cycle = cycle[1:-1].split(" ")
    cycle = [int(x) for x in cycle]
    chr = [i for i in range(1, int(len(cycle)/2) +1)]
    for j in range(0, int(len(cycle)/2)):
        if(cycle[2*j] > cycle[2*j + 1]):
            chr[j] = -chr[j]
    return chr

cycInput = "(2 1 4 3 5 6 8 7 10 9 12 11 14 13 16 15 18 17 20 19 21 22 24 23 26 25 28 27 29 30 31 32 33 34 36 35 38 37 39 40 42 41 43 44 46 45 48 47 49 50 52 51 53 54 56 55 58 57 60 59 62 61 64 63 66 65 68 67 69 70 71 72 74 73 75 76 78 77 80 79 81 82 84 83 85 86 88 87 89 90 91 92 93 94 96 95 97 98 99 100 102 101 104 103 105 106 107 108 109 110 111 112 113 114 116 115 117 118 120 119 121 122 124 123 126 125 127 128 130 129 132 131 133 134)"

print("(", end="")
for i in cycleToChromosome(cycInput):
    if(i > 0):
        print("+", end="")
    if i == cycleToChromosome(cycInput)[-1]:
        print(i, end="")
    else:
        print(i, end=" ")
print(")")
