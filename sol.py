from copy import deepcopy
import sys

sys.setrecursionlimit(100000)
inputfile = open(sys.argv[1]).read()

mat = [line for line in inputfile.strip().split("\n")]
n = len(mat)
m = len(mat[0])

for i in range(n):
    for j in range(m):
        if mat[i][j] == 'S':
            x = i
            y = j

dirs = {}
dirs['.'] = {}
dirs['-'] = {(0, -1), (0, 1)}
dirs['|'] = {(1, 0), (-1, 0)}
dirs['7'] = {(0, -1), (1, 0)}
dirs['J'] = {(0, -1), (-1, 0)}
dirs['L'] = {(0, 1), (-1, 0)}
dirs['F'] = {(0, 1), (1, 0)}

def valid(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

def flip(x, y):
    return (-x, -y)

def get_dir(sym, from_dir):
    tdirs = deepcopy(dirs[sym])
    tdirs.remove(from_dir)
    return list(tdirs)[0]

def advance(x, y, from_dir):
    match mat[x][y]:
        case 'S':
            for (dx, dy) in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                new_x = x + dx
                new_y = y + dy
                if not valid(new_x, new_y): 
                    continue
                if flip(dx, dy) in dirs[mat[new_x][new_y]]:
                    return (new_x, new_y, flip(dx, dy))
                    break
        case _ :
            (dx, dy) = get_dir(mat[x][y], from_dir)
            return (x + dx, y + dy, flip(dx, dy))


a = [[0] * m for i in range(n)]
counter = 1
a[x][y] = counter
from_dir = 0
outside = set()

while(True):
    outside.add((x, y))
    (x, y, from_dir) = advance(x, y, from_dir)
    counter += 1
    if mat[x][y] == 'S':
        break
    a[x][y] = counter

print("Part 1: ", counter // 2)

def touching(x, y):
    sol = set()
    for dx in [0, 1]:
        for dy in [0, 1]:
            if valid(x - dx, y - dy):
                sol.add((x - dx, y - dy))
    return sol

def cuts(cells):
    cells = list(cells)
    if len(cells) < 2:
        return False
    assert len(cells) == 2, cells

    first = a[cells[0][0]][cells[0][1]]
    second = a[cells[1][0]][cells[1][1]]

    dif = abs(first - second)
    return first > 0 and second > 0 and (dif == 1 or dif == counter - 2)
    
visited = [[0] * (m + 1) for i in range(n + 1)]

def dfs(x, y):
    global outside
    visited[x][y] = 1
    touch = touching(x, y)
    outside = outside | touch

    for (dx, dy) in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
        new_x = x + dx
        new_y = y + dy
        if new_x < 0 or new_y < 0 or new_x > n or new_y > m: 
            continue
        if visited[new_x][new_y]:
            continue

        new_touch = touching(new_x, new_y)
        common = touch & new_touch

        if cuts(common):
            continue
        
        dfs(new_x, new_y)

dfs(0, 0)

print("Part 2: ", n * m - len(list(outside)))