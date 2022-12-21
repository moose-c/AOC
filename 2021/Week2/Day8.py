input = open('input.txt', 'r').read().splitlines()
input = [[el.split(' | ')[0].split(' '), el.split(' | ')[1]] for el in input]
"""
ouput on signal wires a - g. Wires connected randomly
formulate hypothesis
"""

def decodeOutput(inp):
    output = inp[1]
    len5 = []
    len6 = []
    for el in inp[0]: 
        if len(el) == 2:
            two = set(el)
        if len(el) == 3:
            seven = set(el)
        if len(el) == 4:
            four = set(el)
        if len(el) == 5:
            len5.append(set(el))
        if len(el) == 6:
            len6.append(set(el))
        if len(el) == 7:
            eight = set(el)
    output = output.replace(''.join(seven.difference(two)), 'A')
    for el in len6:
        if el.intersection(four) == four:
            output = output.replace(''.join(eight.difference(el)), 'E')
    
    return(output.split(' '))


def outputToValue(output):
    d = {'ABCEFG':0, 'CF':1, 'ACDEG':2, 'ACDFG':3, 'BCDF':4, 'ABDFG':5, 'ABDEFG':6, 'ACF':7, 'ABCDEFG':8, 'ABCDFG':9}
    ret = ''
    for val in output:
        ret += str(d[val])
    return(d[output])

count = 0
for el in input:
    count += outputToValue(decodeOutput(el))
    print(count)