import copy
lst = [int(i) for i in open('../input.txt').read().split(',')]

def intcode(a, b, lst):
    inp = copy.deepcopy(lst)
    inp[1] = a
    inp[2] = b
    i = 0
    while i < len(inp):
        if inp[i] == 1:
            inp[inp[i+3]] = inp[inp[i+1]] + inp[inp[i+2]]
            i += 4
        elif inp[i] == 2:
            inp[inp[i+3]] = inp[inp[i+1]] * inp[inp[i+2]]
            i += 4
        elif inp[i] == 99:
            break
    return(inp)

for i in range(100):
    for j in range(100):
        c = intcode(i,j,lst)[0]
        if c == 19690720:
            print(i,j)
            break
print(intcode(12, 2, lst))