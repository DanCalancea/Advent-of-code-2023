import sys, fileinput

CIFRE = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')

sum,unu= 0,0

if len(sys.argv) > 1:
    fil = open(sys.argv[1])
else:
    fil = fileinput.input(files='intrari1p1.txt')

for line in fil:  # citim

    line = line.replace('\n', '')
    nr = 0
    for i in range(9):
        line = line.replace(str(i + 1), CIFRE[i]) # trec toate cifrele in analog

    min, max = 1000, 0
    for i in range(9):
        a = line.find(CIFRE[i])
        if -1 < a <= min:
            unu = i + 1
            min = a

    nr = unu * 10
    for i in range(9):
        a = line.rfind(CIFRE[i])
        if a >= max:
            unu = i + 1
            max = a

    nr += unu
    
    sum += nr

print('rezultat partea 2:', sum)
