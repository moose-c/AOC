raw_input = open('input.txt', 'r').read().splitlines()

llst = []
for line in raw_input:
    a, b = line.split(' ')
    small_lst = [a, b]
    llst.append(small_lst)

def using_code(code):
    pass
    
def Day8_1st(lst = llst):
    acc = 0
    index = 0
    index_lst = []
    while (index not in index_lst) and (index < len(lst)):
        code = lst[index]
        if code[0] == 'acc':
            if code[1][0] == '+':
                acc += int(code[1][1:])
            if code [1][0] == '-':
                acc -= int(code[1][1:])
            index_lst.append(index)
            index += 1         
        elif code[0] == 'nop':
            index_lst.append(index)
            index += 1
        elif code[0] == 'jmp':
            index_lst.append(index)
            if code[1][0] == '+':
                index += int(code[1][1:])
            if code [1][0] == '-':
                index -= int(code[1][1:])
    return(acc, index_lst, index)

#print(Day8_1st())

def Day8_2nd(lst = llst):
    acc = 0
    index = 0
    i = 0
    while i < len(lst):
        code = lst[i]
        copy_lst = lst
        old, change = code[0], code[0]
        if 'jmp' in code[0]:
            change = 'nop'
        elif 'nop' in code[0]:
            change = 'jmp'
        copy_lst[i][0] = change
        acc, b, index = Day8_1st(copy_lst)
        copy_lst[i][0] = old
        if index == len(lst):
            print('succes!')
            break
        if index > len(lst):
            pass
        i += 1
    return(acc)

print(Day8_2nd())

#2187 is te hoog
#809 is te laag
