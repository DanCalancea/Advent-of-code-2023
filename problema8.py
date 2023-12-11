import sys, fileinput

parttwo = True
rezultat = 0
first = True
traseu = dict()

starts = []
rezultate = []

if len(sys.argv) > 1:
    fil = open(sys.argv[1])
else:
    fil = fileinput.input(files='intrari8p1.txt')

for line in fil:  # citim

    line = line.replace('\n', '')
    if first:
        direction = [0 if x == "L" else 1 for x in line]
        first = False
        continue
    if len(line) < 2: continue
    line = line.replace(' = (', ',')
    line = line.replace(', ', ',')
    line = line.replace(')', '')

    unu, doi, trei = line.split(',')
    if unu[-1] == "A": starts.append(unu)
    traseu[unu] = (doi, trei)

for x in starts:
    rezultat = 0
    indicator = 0
    destination = False
    start = x
    while not destination:
        catre = traseu[start][direction[indicator]]
        rezultat += 1
        if catre[-1] == 'Z':
            destination = True
        else:
            indicator = indicator + 1 if indicator < len(direction) - 1 else 0
            start = catre

    rezultate.append(rezultat)
minrez=min(rezultate)
divizor = 1
for j in range(2,  minrez // 2):  # cmmdc
    di = True
    for x in rezultate:
        if x // j != x / j:
            di = False
            break
    if di: divizor = j

rezultat = rezultate[0]
for i in range(1, len(rezultate)):
    rezultat *= rezultate[i] // divizor

if parttwo:
    print('rezultat partea a 2a :', rezultat)
else:
    print('rezultat partea a 1a :', rezultat)
