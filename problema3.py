import sys, fileinput


def verific(x, y):
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            if intrare[x + i][y + j] == '*':
                return 1, x + i, y + j

    return 0, 0, 0


intrare, matrix = [], []

sum, summin, id = 0, 0, 1

primul = True
if len(sys.argv) > 1:
    fil = open(sys.argv[1])
else:
    fil = fileinput.input(files='intrari3p1.txt')

for line in fil:  # citim
    if primul:
        intrare.append(['.' for i in range(len(line) + 3)])
        matrix.append(['' for i in range(len(line) + 3)])
        primul = False

    line = line.replace('\n', '')
    line = '.' + line + '..'
    intrare.append([line[i] for i in range(len(line))])
    matrix.append(["" for i in range(len(line))])

intrare.append(['.' for i in range(len(line) + 3)])
matrix.append(['' for i in range(len(line) + 3)])

for y in range(1, len(intrare) - 1):
    numar = ''
    valid = False
    for x in range(1, len(intrare[1]) - 1):
        simb = intrare[y][x]
        if 58 > ord(simb) > 47:
            numar += simb
            if not valid:
                bun, ux, uy = verific(y, x)
                if bun > 0: valid = True

        else:
            if numar == "": continue
            if valid:
                matrix[ux][uy] += numar + ','
                print(numar)

            numar = ''
            valid = False

for i in range(len(matrix)):
    for j in range(len(matrix[1])):
        no = []
        if len(matrix[i][j]) == 0: continue
        no = matrix[i][j].split(',')
        print(no)
        if len(no) < 3: continue
        sum += int(no[0]) * int(no[1])

print('rezultat partea 2:', sum)
