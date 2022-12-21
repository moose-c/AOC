from math import *
import numpy as np
raw_input = open('input.txt').read().splitlines()

def Day14_1st():
    mem = {}
    mask = ''
    for line in raw_input:
        if line[0:4] == 'mask':
            mask = line[7:]
        else:
            proc = line.split('] = ')
            a, b = int(proc[0][4:]), int(proc[1])
            res = apply_mask1(b, mask)
            mem[a] = res
    return(mem)
            

def apply_mask1(n, mask):
    b = bin(n)[2:]
    while len(b) < 36:
        b = '0' + b
    for i in range(36):
        if mask[i] != 'X':
            b = b[:i] + mask[i] + b[i+1:]
    res = int(b, 2)
    return(res)
                
##copymem = Day14_1st()
##print(sum(copymem.values()))
def Day14_2nd():
    mem = {}
    mask = ''
    for line in raw_input:
        if line[0:4] == 'mask':
            mask = line[7:]
        else:
            proc = line.split('] = ')
            a, b = int(proc[0][4:]), int(proc[1])
            res = apply_mask2(a, mask)
            for pos in res:
                mem[int(pos)] = b
    return(mem)
            

def apply_mask2(n, mask):
    b = bin(n)[2:]
    while len(b) < 36: b = '0' + b
    for i in range(36):
        if mask[i] in 'X1': b = b[:i] + mask[i] + b[i+1:]
    xs = 0
    for el in b:
        if el == 'X': xs += 1
    brlst = []
    for i in range(2**xs):
        s = bin(i)[2:]
        while len(s) < xs: s = '0' + s
        br = ''
        i = 0
        for el in b:
            if el == 'X':
                br += s[i]
                i += 1
            else: br += el
        brlst.append(br)
    rlst = [int(br, 2) for br in brlst]
    return(rlst)

mask = '000000000000000000000000000000X1001X'
n = 24

rlst = apply_mask2(n, mask)

res = Day14_2nd()
print(sum(res.values()))

#3615013500127401 is too high
#4254673508445
