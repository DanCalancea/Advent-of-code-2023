import sys, fileinput
import numpy as np
track = []

rezultat = 0
first = True
intrare = []

sys.setrecursionlimit(100000)


def seek(point, traseu, leftt, rightt):
    global track, gata
    if gata: return
    for unde in nextmove:
        indice, semne, left, right = nextmove[unde]
        nextpoint = (point[0] + indice[0], point[1] + indice[1])
        leftpoint = (point[0] + left[0], point[1] + left[1])
        rightpoint = (point[0] + right[0], point[1] + right[1])
        if nextpoint in traseu: continue
        if intrare[nextpoint[0]][nextpoint[1]] in semne:

            newtraseu = traseu.copy()

            newleft = leftt.copy()
            newright = rightt.copy()
            newtraseu.append(nextpoint)
            newleft.append(leftpoint)
            newright.append(rightpoint)

            if intrare[nextpoint[0]][nextpoint[1]] == 'S' and point in validpoint and len(newtraseu) > 4:
                track.append([newtraseu, newleft, newright])
                gata = True
                return

            seek(nextpoint, newtraseu, newleft, newright)

        else:
            continue


nextmove = {'up': [(-1, 0), ('7', '|', 'F', 'S'), (-1, -1), (-1, 1)], 'down': [(1, 0), ('|', 'L', 'J', 'S'),
                                                                               (1, 1), (1, -1)],
            'left': [(0, -1), ('-', 'L', 'F', 'S'), (1, -1), (-1, -1)],
            'right': [(0, 1), ('-', '7', 'J', 'S'), (-1, 1), (1, 1)]}

# ----------------------------------parse input in a matrix

if len(sys.argv) > 1:
    fil = open(sys.argv[1])
else:
    fil = fileinput.input(files='intrari10p1.txt')

for line in fil:  # citim
    line = line.replace('\n', '')
    line = 'AA' + line + 'AA'
    if first:
        intrare.append(['A' for x in line])
        intrare.append(['A' for x in line])
        first = False

    intrare.append([x for x in line])

intrare.append(['A' for x in line])
intrare.append(['A' for x in line])


matrix= np.copy(intrare)


for y in range(len(intrare)):  # locate 'S'
    for x in range(len(intrare[0])):
        if intrare[y][x] == 'S':
            start = [y, x]

gata = False
validpoint = []

for unde in nextmove:
    indice, semne, left, right = nextmove[unde]
    nextpoint = (start[0] + indice[0], start[1] + indice[1])
    if intrare[nextpoint[0]][nextpoint[1]] in semne: validpoint.append(nextpoint)

print('calculez')
seek(start, [], [], [])

rezultat = len(track[0][0]) // 2

for j in track[0][0]:
    intrare[j[0]][j[1]] = '*'

trebuie = True
gasitout = True
a = 0
nu = True
while trebuie:
    trebuie = False
    for y in range(2, len(intrare) - 2):
        for x in range(2, len(intrare[0]) - 2):
            if intrare[y][x] not in ('A', '*', 'I'):
                for i in nextmove:

                    indice, semn, left, right = nextmove[i]
                    yy, xx = indice[0], indice[1]

                    if intrare[yy + y][xx + x] == 'A':
                        trebuie = True
                        intrare[y][x] = 'A'
                    if intrare[yy + y][xx + x] == 'I':
                        trebuie = True
                        intrare[y][x] = 'I'

    for y in range(len(intrare) - 1, 1, -1):
        for x in range(len(intrare[0]) - 1, 1, -1):
            if intrare[y][x] not in ('A', '*', 'I'):
                for i in nextmove:
                    indice, semn, left, right = nextmove[i]
                    yy, xx = indice[0], indice[1]

                    if intrare[yy + y][xx + x] == 'A':
                        trebuie = True
                        intrare[y][x] = 'A'
                    if intrare[yy + y][xx + x] == 'I':
                        trebuie = True
                        intrare[y][x] = 'I'

    if gasitout:
        for j in track[0][1]:
            if intrare[j[0]][j[1]] == 'A':
                aka, iaka = 1, 2
                gasitout = False
        for j in track[0][2]:
            if intrare[j[0]][j[1]] == 'A':
                aka, iaka = 2, 1
                gasitout = False

        if not gasitout:

            for j in track[0][aka]:
                if intrare[j[0]][j[1]] == '*': continue
                intrare[j[0]][j[1]] = 'A'
                trebuie = True
            for j in track[0][iaka]:
                if intrare[j[0]][j[1]] == '*': continue
                intrare[j[0]][j[1]] = 'I'
                trebuie = True
    a += 1

print('aaaaa', a)
leftout = False
rightout = False
numar = 0
numar2 = 0

for y in range(2, len(intrare) - 1):
    for x in range(2, len(intrare[0]) - 1):
        if intrare[y][x] != 'A' and intrare[y][x] != '*' and intrare[y][x] != 'I':
            print(y, x, intrare[y][x])
            print(intrare[y - 1][x - 1], intrare[y - 1][x], intrare[y][x + 1] ,'  ',matrix[y - 1][x - 1], matrix[y - 1][x], matrix[y][x + 1])
            print(intrare[y][x - 1], intrare[y][x], intrare[y][x + 1] ,'  ',matrix[y][x - 1], matrix[y][x], matrix[y][x + 1])
            print(intrare[y + 1][x - 1], intrare[y + 1][x], intrare[y + 1][x + 1] ,'  ',matrix[y + 1][x - 1], matrix[y + 1][x], matrix[y+1][x + 1])
        if intrare[y][x] != 'A' and intrare[y][x] != '*':
            numar += 1

        if intrare[y][x] == 'I': numar2 += 1

print('rezultat partea a 2a :', numar, numar2)

print('rezultat partea a 1a :', rezultat)
