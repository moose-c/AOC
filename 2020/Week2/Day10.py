import numpy as np
r_in = [0]
r_in += open('input.txt').read().splitlines()
r_in = list(map(int,r_in))
r_in.append(max(r_in)+3)
#r_in = [0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
#32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 48, 49, 52]
def Day10_1st(lst = r_in):
    lst = sorted(lst)
    res_1, res_2, res_3 = 0, 0, 0
    dif = []
    for i in range(len(lst)-1):
        i += 1
        dif.append(lst[i] - lst[i-1])
    return(dif)

res = Day10_1st()


#2232 is not right
#2263
def opties(lst):
    if lst[0] == 0:
        return(7)
    elif len(lst) == 3 or len(lst) == 2:
        return(1)
    elif len(lst) == 4:
        return(2)
    elif len(lst) == 5:
        return(4)
    elif len(lst) == 6:
        return(7)
    elif len(lst) == 7:
        return(13)
    

def Day10_2nd(lst = r_in):
    lst = sorted(lst)
    dif = Day10_1st()
    i = 0
    reslst = []
    while len(lst) > 2:
        if i < len(dif):
            if dif[i] == 3:
                sublst = lst[:i+1] #len sublst = i
                lst = lst[i:]
                dif = dif[i:]
                i = 0
                print(sublst)
                reslst.append(opties(sublst))
        i += 1
    return(reslst)

res = Day10_2nd()
res1, res2 = res[int(len(res)/2):], res[:int(len(res)/2)]
s1, s2 = np.prod(res1), np.prod(res2)
print(np.prod(res))
            
# 1509949440 is to low
# 1886490624 also to low
