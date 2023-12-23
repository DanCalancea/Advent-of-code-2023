import sys, fileinput

parttwo = True
rezultat = 0
nr = 0
univers = []
fara = []
indice = 999999 if parttwo else 1

if len(sys.argv) > 1:
    fil = open(sys.argv[1])
else:
    fil = fileinput.input(files='intrari11p1.txt')

for line in fil:  # citim
    nuare = True
    line = line.replace('\n', '')

    for i in range(len(line)):
        if line[i] == '#':
            univers.append([nr, i])
            nuare = False
            lung = len(line)
    if nuare: nr += indice
    nr += 1

for i in range(lung):
    nuare = True
    for y, x in univers:
        if x == i:
            nuare = False

    if nuare: fara.append(i)
fara.reverse()

for i in fara:
    for j in range(len(univers)):
        y, x = univers[j]
        if x > i:
            univers[j] = (y, x + indice)

for y, x in univers:
    for yy, xx in univers:
        if yy == y and xx == x: continue
        rezultat += (abs(yy - y) + abs(xx - x))

if parttwo:
    print('rezultat partea a 2a :', rezultat // 2)
else:
    print('rezultat partea a 1a :', rezultat // 2)
