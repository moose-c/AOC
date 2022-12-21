inp = open('input.txt').read().splitlines()

def is_sum(nb, lst = inp):
    i = 0
    while i < 25:
        j = 0
        while j < i:
            comp = int(lst[i]) + int(lst[j])
            if comp == nb:
                return(True)
            j += 1
        i += 1
    return(False)
                    

def Day8_1st():
    copy = inp
    while True:
        nb = int(copy[25])
        if not is_sum(nb, copy):
            return(nb)
        else:
            copy = copy[1:]
            
goal = Day8_1st()

def Day8_2nd():
    i = 0
    while int(inp[i]) < goal:
        s = 0
        j = 0
        slst = []
        while s < goal:
            s += int(inp[i+j])
            slst.append(int(inp[i+j]))
            if s == goal:
                return(slst)
            j += 1

        i += 1

ans = Day8_2nd()
#20 =/ right
