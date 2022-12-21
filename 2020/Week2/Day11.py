raw_input = open('input.txt').read().splitlines()
lst = []
for row in raw_input:
    lst.append('e' + row + 'e')
elst = ['e'*len(lst[1])]
lst = elst + lst + elst


def count_adj1(row, col, lst):
    nb = 0
    if lst[row][col-1] == '#':
        nb += 1
    if lst[row][col+1] == '#':
        nb += 1
    if lst[row-1][col-1] == '#':
        nb += 1
    if lst[row-1][col] == '#':
        nb += 1
    if lst[row-1][col+1] == '#':
        nb += 1
    if lst[row+1][col-1] == '#':
        nb += 1
    if lst[row+1][col] == '#':
        nb += 1
    if lst[row+1][col+1] == '#':
        nb += 1
    return(nb)

def count_adj2(row, col, lst):
    zlst = 'Le'
    nb = 0
    for i in range(3):
        i -= 1
        for j in range(3):
            bo = True
            j -= 1
            r = 1
            while True:
                if not (i == 0 and j == 0):
                    if lst[row+i*r][col+j*r] == '#' and bo:
                        nb += 1
                        bo = False
                    elif lst[row+i*r][col+j*r] in zlst and bo:
                        bo = False
                    r += 1
                    if not bo:
                        break
                else:
                    break
    return(nb)  

def Day11_1st_2nd(count_adj):
    res2 = lst
    while True:
        prevres = res2
        res1, res2 = ['']*len(prevres), ['']*len(prevres)
        r = 0
        for row in prevres:
            c = 0
            for seat in row:
                if seat == 'L':
                    if count_adj(r, c, prevres) == 0:
                        res1[r] += '#'
                    else:
                        res1[r] += seat
                else:
                    res1[r] += seat
                c += 1
            r += 1
        r = 0
        for row in res1:
            c = 0
            for seat in row:
                if seat == '#':
                    if count_adj(r, c, res1) >= 5:
                        res2[r] += 'L'
                    else:
                        res2[r] += seat
                else:
                    res2[r] += seat
                c += 1
            r += 1
        if res2 == prevres:
            break
    return(res2)

res = Day11_1st_2nd(count_adj2)
nb = 0
for row in res:
    nb += row.count('#')
print(nb)

#7423 is to high
