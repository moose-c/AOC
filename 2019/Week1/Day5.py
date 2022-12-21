import copy
lst = [int(i) for i in open('../input.txt').read().split(',')]

def intcode(pos, lst):
    posup = 4
    Param = lst[pos]
    if Param == 99:
        posup = -1
    else:
        op, c, b, a = ProcessParameter(Param, pos, lst)
        if op == 1:
            lst[a] = c + b ## weet niet of dit met lsts werkt
        elif op == 2:
            lst[a] = c * b ## idem
        elif op == 3:
            inp = input("enter input")
            lst[lst[pos+1]] = int(inp)
            posup = 2
        elif op == 4:
            output = c
            print('output = ', output)
            #yn = input('do you want to continue? (y/n)')
            yn = 'y'
            if yn == 'n':
                posup = -1
            else:
                posup = 2
        elif op == 5:
            if c != 0:
                posup = b - pos
            else:
                posup = 3
        elif op == 6:
            if c == 0:
                posup = b - pos
            else:
                posup = 3
        elif op == 7:
            if c < b:   lst[a] = 1
            else:   lst[a] = 0
        elif op == 8:
            if c == b:  lst[a] = 1
            else:   lst[a] = 0
        else:
            print(op)
            print('what')
            posup = -1
    return(posup, lst)

def ProcessParameter(n, pos, lst):
    strn = '00000'+ str(n)
    nblst1 = [1,2,5,6,7,8]
    nblst2 = [1,2,7,8]
    op = int(strn[-2:])
    c, ci = int(strn[-3]), lst[pos+1]
    b, bi = int(strn[-4]), lst[pos+2]
    a, ai = int(strn[-5]), pos+3
    if c == 0:
        ci = lst[ci]
    if b == 0 and op in nblst1:
        bi = lst[bi]
    if a == 0 and op in nblst2:
        ai = lst[ai]

    return(op, ci, bi, ai)

def programm(lst):
    i = 0
    while i < len(lst):
        posup, lst = intcode(i, lst)
        if posup == -1:
            print('programm ends')
            break
        else:
            i += posup
    
    

programm(lst)

