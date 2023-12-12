import sys, fileinput

parttwo = True
rezultat = 0
first = True
intrare = []


def operation(L, suma, semn):
    global ax
    ax = suma

    if sum(L) == 0:
        return int(ax)

    uma = []
    for x in range(len(L) - 1):
        uma.append(L[x + 1] - L[x])
    suma += uma[indice] * semn
    semn = semn * factor
    operation(uma, suma, semn)


if len(sys.argv) > 1:
    fil = open(sys.argv[1])
else:
    fil = fileinput.input(files='intrari9p1.txt')

for line in fil:  # citim

    line = line.replace('\n', '')
    intrare.append([int(x) for x in line.split(' ')])

rezultat = 0

if parttwo:
    indice = 0
    factor = -1
else:
    indice = -1
    factor = 1

for l in intrare:
    unu = operation(l, l[indice], factor)

    rezultat += ax

if parttwo:
    print('rezultat partea a 2a :', rezultat)
else:
    print('rezultat partea a 1a :', rezultat)
