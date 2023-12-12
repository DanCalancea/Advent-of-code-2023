import sys, fileinput

parttwo = False
rezultat=0
first=True
traseu=dict()


if len(sys.argv) > 1:
    fil = open(sys.argv[1])
else:
    fil = fileinput.input(files='intrari8p1.txt')

for line in fil:  # citim

    line = line.replace('\n', '')
    if first:
        direction=[ 0 if x=="L" else 1 for x in line]
        print (direction)
        first=False
        continue
    if len(line) <2 : continue
    line = line.replace(' = (', ',')
    line = line.replace(', ', ',')
    line = line.replace(')', '')

    unu, doi ,trei = line.split(',')
   
    traseu[unu]=(doi,trei)
    print (traseu)

indicator=0
destination=False
start='AAA'

while not destination:
    catre=traseu[start][direction[indicator]]
    rezultat+=1
    if catre =='ZZZ':
        destination=True
    else :
        indicator = indicator + 1 if indicator <len(direction)-1 else 0
        start=catre


if parttwo:
    print('rezultat partea a 2a :', rezultat)
else:
    print('rezultat partea a 1a :', rezultat)
