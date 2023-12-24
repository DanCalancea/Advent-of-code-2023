import sys, fileinput

from itertools import product

parttwo = False
rezultat = 0
nr = 0

if len(sys.argv) > 1:
    fil = open(sys.argv[1])
else:
    fil = fileinput.input(files='intrari12p1.txt')

for line in fil:  # citim

    line = line.replace('\n', '')
    unu, doi = line.split(' ')
    doibun = [int(i) for i in doi.split(',')]
    trei = ['#' * i + '.' for i in doibun]
    trei[-1] = trei[-1][0:-1]
    lung3 = (sum(len(i) for i in trei))
    diff = len(unu) - lung3
    cite = len(doibun)

    a = [i for i in range(diff + 1)]

    l = list(filter(lambda x: sum(x) == diff, product(a, repeat=cite + 2)))

    citevariante = 0
    lotvariante = []
    for i in l:
        varianta = '.' * i[0]
        for x in range(len(trei)):
            varianta += trei[x] + '.' * i[x + 1]
        varianta += '.' * i[-1]
        # print (len(varianta),varianta)
        valid = True
        if varianta in lotvariante: continue
        for y in range(len(varianta)):
            if varianta[y] == unu[y] or unu[y] == '?':
                zero = 0
            else:
                valid = False
        lotvariante.append(varianta)
        if valid:
            citevariante += 1

    print(citevariante)
    rezultat += citevariante
if parttwo:
    print('rezultat partea a 2a :', rezultat)
else:
    print('rezultat partea a 1a :', rezultat)
