inp = [0,12,6,13,20,1,17]

def Day15_1st(inp):
    previous_numbers = {el : inp.index(el)+1 for el in inp[:-1]}
    previous = inp[-1]
    current = 0
    turn = len(inp)
    print(previous_numbers)
    while turn < 30000000:
        if previous in previous_numbers:
            current = turn - previous_numbers[previous]
        else:
            current = 0
        previous_numbers[previous] = turn
        turn += 1
        previous = current
    print(previous)
    

#res = Day15_1st(inp)

