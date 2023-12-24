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

    l = set(filter(lambda x: sum(x) == diff, product(a, repeat=cite + 1)))

    citevariante = 0

    for u in l:
        varianta = '.' * u[0]
        for x in range(len(trei)):
            varianta += trei[x] + '.' * u[x + 1]

        valid = True

        for y in range(len(unu)):

            if varianta[y] != unu[y] and unu[y] != '?':
                valid=False
                break

        if valid:
            citevariante += 1



    rezultat +=citevariante
if parttwo:
    print('rezultat partea a 2a :', rezultat)
else:
    print('rezultat partea a 1a :', rezultat)
