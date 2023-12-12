import sys, fileinput

cards = []
cardsvalue = []
bid = []

carti = ('A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2')


def power1(hand):
    c = set(x for x in hand)
    if len(c) == 5:
        power = 0
    elif len(c) == 4:
        power = 10 ** 11
    elif len(c) == 3:
        trei = False
        for x in carti:
            if hand.count(x) == 3: trei = True
        if trei:
            power = 10 ** 13
        else:
            power = 10 ** 12
    elif len(c) == 2:
        full = False
        for x in carti:
            if hand.count(x) == 4: full = True
        if full:
            power = 10 ** 15
        else:
            power = 10 ** 14
    elif len(c) == 1:
        power = 10 ** 16

    for x in (0, 1, 2, 3, 4):
        power += valoare[hand[x]] * (10 ** (9 - x * 2))

    return power


def power2(hand):
    if 'J' not in hand:
        return power1(hand)
    nrj = hand.count('J')
    c = set(x for x in hand)
    if len(c) == 5:  # -------------------------------------
        power = 10 ** 11
    elif len(c) == 4:
        if nrj == 1:
            power = 10 ** 13
        if nrj == 2:
            power = 10 ** 13
    elif len(c) == 3:
        if nrj == 1:
            trei = False
            for x in carti:
                if hand.count(x) == 3: trei = True
            power = 10 ** 15 if trei else 10 ** 14
        elif nrj == 2:  # --ar fi full 4 buc
            power = 10 ** 15
        elif nrj == 3:
            power = 10 ** 15

    elif len(c) <= 2:  # ---------------------------------
        power = 10 ** 16

    for x in (0, 1, 2, 3, 4):
        power += valoare[hand[x]] * (10 ** (9 - x * 2))

    return power


parttwo = True

if not parttwo:
    valoare = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3,
               '2': 2}
else:
    valoare = {'A': 14, 'K': 13, 'Q': 12, 'T': 11, '9': 10, '8': 9, '7': 8, '6': 7, '5': 6, '4': 5, '3': 4, '2': 3,
               'J': 2}

if len(sys.argv) > 1:
    fil = open(sys.argv[1])
else:
    fil = fileinput.input(files='intrari7p1.txt')

for line in fil:  # citim

    line = line.replace('\n', '')
    unu, doi = line.split(' ')
    cards.append(unu)
    ulsa = power2(unu) if parttwo else power1(unu)
    cardsvalue.append(ulsa)
    bid.append((ulsa, int(doi)))

topcardsvalue = sorted(cardsvalue)

rezultat = 0

for x, y in bid:
    rezultat += y * (topcardsvalue.index(x) + 1)

if parttwo:
    print('rezultat partea a 2a :', rezultat)
else:
    print('rezultat partea a 1a :', rezultat)
