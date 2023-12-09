import sys, fileinput

seeds, ss, sf, wf, wl, lt, th, hm = [], [], [], [], [], [], [], []
unit = ('seeds', 'ss', 'sf', 'wf', 'wl', 'lt', 'th', 'hm')

primul = True
unde=0
if len(sys.argv) > 1:
    fil = open(sys.argv[1])
else:
    fil = fileinput.input(files='intrari5p1.txt')

for line in fil:  # citim

    line = line.replace('\n', '')
    if primul:
        primul = False
        line = line[7:]
        seeds = [int(x) for x in line.split(' ')]
        continue
    citit = [x for x in line.split(' ')]

    if len(citit) == 1:
        unde += 1
        continue
    if len(citit) < 3:
        continue
    eval(unit[unde]).append([int(x) for x in citit])

rezultate = []

for i in seeds:
    ulsa = i
    for k in range(1, 8):
        cale = ulsa
        for j in eval(unit[k]):
            if j[1] <= ulsa <= j[1] + j[2]:
                cale = j[0] + ulsa - j[1]
                break
        ulsa = cale
    rezultate.append(cale)

print('rezultat partea 1:', min(rezultate))
minim = -1

for i in range(int(1E8)):
    valid = False
    ulsa = i
    for k in range(6, 0, -1):
        cale = ulsa
        for j in eval(unit[k]):
            if j[0] <= ulsa <= j[0] + j[2]:
                cale = j[1] + ulsa - j[0]
                valid = True
                break
        if not valid: break
        ulsa = cale

    if valid:
        for x in range(0, len(seeds), 2):
            for y in range(seeds[x], seeds[x] + seeds[x + 1]):
                if y == cale:
                    minim = i
                    break
    if minim >= 0:
        break

print('rezultat partea a 2a :', minim)
