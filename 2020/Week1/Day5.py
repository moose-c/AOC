lst = open('input.txt', 'r').read().split('\n')

def calc_seat(st):
    rows = st[0:8]
    cols = st[7:10]
    rowf,rowb = 0, 127
    i = 0
    while i < 7:
        if rows[i] == 'B':
            rowf += 64/(2**i)
        else:
            rowb -= 64/(2**i)
        i += 1
    if rows[i] == 'B':
        row = rowb
    else:
        row = rowf
    coll, colr = 0, 7
    j = 0
    while j < 2:
        if cols[j] == 'R':
            coll += 4/(2**j)
        else:
            colr -= 4/(2**j)
        j += 1
    if cols[j] == 'R':
        col = colr
    else:
        col = coll
    seat = 8*row + col
    return(seat)
    

def Day5_1st():
    maxseat = 0
    for s in lst:
        seat = calc_seat(s)
        if seat > maxseat:
            maxseat = seat
    return(maxseat)

def Day5_2nd():
    los = []
    for s in lst:
        los.append(int(calc_seat(s)))
    maxseat = int(Day5_1st())
    ls = set(los)
    comp = set([i for i in range(maxseat)])
    print(comp.difference(ls))
test1 = 'BFFFBBFRRR'
print(Day5_2nd())
