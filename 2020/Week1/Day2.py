lst = open('input.txt', 'r').read().splitlines()

def Day2_1st():
    ans = 0
    for i in lst:
        a,b,c = i.split()
        int1f, int2f = a.split('-')
        int1 = int(int1f)
        int2 = int(int2f)
        comp = 0
        for el in c:
            if el == b[0]:
                comp += 1
        if int1 <= comp <= int2:
            ans += 1
    print(ans)
    return

def Day2_2nd():
    ans = 0
    for i in lst:
        a,b,c = i.split()
        int1f, int2f = a.split('-')
        int1 = int(int1f)
        int2 = int(int2f)
        if c[int1-1] == b[0] and c[int2-1] != b[0]:
            ans += 1
        if c[int1-1] != b[0] and c[int2-1] == b[0]:
            ans += 1
    print(ans)
    return
                
                    
        




