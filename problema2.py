import sys, fileinput

maxim = {'green': 13, 'blue': 14, 'red': 12}

sum, summin, id = 0, 0, 1

if len(sys.argv) > 1:
    fil = open(sys.argv[1])
else:
    fil = fileinput.input(files='intrari2p1.txt')

for line in fil:  # citim
    bun = True
    line = line.replace('\n', '')
    line = line.replace('Game ' + str(id) + ': ', '')
    line = line.replace(', ', ',')
    line = line.replace('; ', ',')
    vector = line.split(',')

    minim = {'green': 1, 'blue': 1, 'red': 1}
    for i in range(len(vector)):
        cuplu = vector[i].split(' ')
        if int(cuplu[0]) > minim[cuplu[1]]:
            minim[cuplu[1]] = int(cuplu[0])

        if int(cuplu[0]) > maxim[cuplu[1]]:
            bun = False
    summin += minim['green'] * minim['blue'] * minim['red']
    if bun:
        sum += id
    id += 1

print('rezultat partea 1:', sum)
print('rezultat partea 2:', summin)
