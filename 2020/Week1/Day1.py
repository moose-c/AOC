lst1 = open('input.txt', 'r').read().splitlines()

lst = list(map(int,lst1))
print(lst)

def Day1_first_star():
    i = 0
    j = 0
    for i in lst:
        for j in lst:
            if j > i:
                if j+i == 2020:
                    print(i,j)
                    print(i*j)
                    return
    

def Day1_second_star():
    i = 0
    j = 0
    k = 0
    for i in lst:
        for j in lst:
            for k in lst:
                if k > j > i:
                    if k + j + i == 2020:
                        print(k,j,i)
                        print(k*j*i)
                        return
