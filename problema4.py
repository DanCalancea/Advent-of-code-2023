import sys, fileinput

score, cards = [], []

sum, sumcard = 0, 0

if len(sys.argv) > 1:
    fil = open(sys.argv[1])
else:
    fil = fileinput.input(files='intrari4p1.txt')

for line in fil:  # citim

    line = line.replace('\n', '')
    line = line.replace(' | ', '|')
    line = line.replace('  ', ' ')

    line = line[9:]
    line = line.strip()
    unu, doi = line.split('|')
    set1 = {i for i in unu.split(' ')}
    set2 = {i for i in doi.split(' ')}
    setcastig = set1 & set2
    cite = len(setcastig)
    score.append(cite)
    cards.append(1)
    if cite > 0:
        sum += (2 ** (len(setcastig) - 1))

for i in range(len(score)):
    for j in range(score[i]):
        if i + j + 1 <= len(cards):
            cards[i + j + 1] += cards[i]

for i in cards:
    sumcard += i

print('rezultat partea 1:', sum)
print('rezultat partea 2:', sumcard)
