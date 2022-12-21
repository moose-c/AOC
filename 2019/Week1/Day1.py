lst = [int(i) for i in open("..\input.txt").read().splitlines()]

res = 0 
for el in lst:
    add = (el//3)-2
    while add>0:
        res += add
        add = add//3-2
res