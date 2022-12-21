from math import *
import numpy as np
lst = open('input.txt').read().splitlines()

intlst = []
sublst = lst[1].split(',')
t = 0
for el in sublst:
    if el != 'x':
        intlst.append((int(el), t))
    t += 1
intlst = [(7, 0), (13, 1), (59, 4), (31, 6), (19, 7)]
        

def Day13_1st():
    t = int(lst[0])
    res = []
    for inp in intlst:
        el = inp[0]
        m = 1
        while True:
            nb = el*m
            if nb > t:
                break
            m += 1
        res.append((el, nb - t))
    return(res)

def Day13_2nd():
    nlst = []
    tlst = []
    bignlst = []
    for el in intlst:
        nlst.append(el[0])
        tlst.append(el[1])
    for nb in nlst:
        n = 1
        for el in nlst:
            if el != nb:
                n *= el
        bignlst.append(n)
    print(nlst, tlst)
    bign = 1
    for el in nlst:
        bign *= el
    rlst = []
    for i in range(len(intlst)):
        rlst.append(tlst[i]*(bignlst[i]**(nlst[i]-1)))
    rlst[0] = 0
    print(rlst)
    res1 = sum(rlst)
    print(res1)
    print(bign)
    res = res1 % bign
    return(res)

#552262121348283 is too low
#1024220991808692 is too high
    
            
#lst1, lst2, com = lcm(24, 40)
ans = Day13_1st()

nlst = Day13_2nd()
