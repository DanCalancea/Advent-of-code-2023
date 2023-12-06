import sys, fileinput

def verific(x,y):

    for i in (-1,0,1):
        for j in (-1,0,1):
            if (ord(intrare[x+i][y+j])<48 or ord(intrare[x+i][y+j])>57) :
                if ord(intrare[x+i][y+j])!=46:
                    return True
    return False

intrare=[]

sum, summin, id = 0, 0, 1

primul=True

if len(sys.argv) > 1:
    fil = open(sys.argv[1])
else:
    fil = fileinput.input(files='intrari3p1.txt')

for line in fil:  # citim
    if primul :
        intrare.append(['.' for i in range (len(line)+3)])
        primul=False

    line = line.replace('\n', '')
    line='.'+line+'..'
    intrare.append([line[i] for i in range(len(line))])

intrare.append(['.' for i in range (len(line)+3)])





for y  in range (1,len(intrare)-1):
    numar = ''
    valid=False
    for x in range(1,len(intrare[1])-1):
        simb=intrare[y][x]
        if 58>ord(simb)>47:
            numar+=simb
            if verific(y,x):
                valid=True
        else:
            if numar=="" : continue
            if valid :sum+=int(numar)
            
            numar=''
            valid=False




print('rezultat partea 1:', sum)

